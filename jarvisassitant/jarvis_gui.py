import pygame
import math
import sys
from config import *

class JarvisGUI:
    def __init__(self):
        """Initialize JARVIS GUI"""
        pygame.init()
        
        # Create window
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("J.A.R.V.I.S - Just A Rather Very Intelligent System")
        
        # Fonts
        self.title_font = pygame.font.Font(None, 72)
        self.text_font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)
        
        # Animation variables
        self.pulse_angle = 0
        self.circle_radius = 80
        self.particles = []
        
        # Status
        self.status = "Initializing..."
        self.command_text = ""
        self.response_text = ""
        
        # Clock for FPS
        self.clock = pygame.time.Clock()
        
    def create_particles(self, count=5):
        """Create particle effects"""
        for _ in range(count):
            angle = math.radians(self.pulse_angle + (_ * 72))
            particle = {
                'x': WINDOW_WIDTH // 2,
                'y': WINDOW_HEIGHT // 2,
                'vx': math.cos(angle) * 2,
                'vy': math.sin(angle) * 2,
                'life': 60
            }
            self.particles.append(particle)
    
    def update_particles(self):
        """Update particle positions"""
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            
            if particle['life'] <= 0:
                self.particles.remove(particle)
    
    def draw_circle_animation(self, is_listening=False, is_speaking=False):
        """Draw animated circle (JARVIS core)"""
        center_x = WINDOW_WIDTH // 2
        center_y = WINDOW_HEIGHT // 2 - 100
        
        # Pulsing effect
        self.pulse_angle += 3
        pulse = math.sin(math.radians(self.pulse_angle)) * 10
        current_radius = self.circle_radius + pulse
        
        # Draw outer rings
        for i in range(3):
            alpha = 100 - (i * 30)
            radius = current_radius + (i * 20)
            color = (*ACCENT_COLOR, alpha)
            
            # Draw circle segments
            for angle in range(0, 360, 10):
                start_angle = math.radians(angle + self.pulse_angle)
                end_angle = math.radians(angle + 5 + self.pulse_angle)
                
                start_x = center_x + math.cos(start_angle) * radius
                start_y = center_y + math.sin(start_angle) * radius
                end_x = center_x + math.cos(end_angle) * radius
                end_y = center_y + math.sin(end_angle) * radius
                
                pygame.draw.line(self.screen, ACCENT_COLOR, 
                               (start_x, start_y), (end_x, end_y), 3)
        
        # Center circle
        if is_listening:
            color = (255, 100, 100)  # Red when listening
            self.create_particles(2)
        elif is_speaking:
            color = (100, 255, 100)  # Green when speaking
            self.create_particles(2)
        else:
            color = ACCENT_COLOR
        
        pygame.draw.circle(self.screen, color, (center_x, center_y), 
                          int(current_radius * 0.6), 0)
        pygame.draw.circle(self.screen, BACKGROUND_COLOR, (center_x, center_y), 
                          int(current_radius * 0.4), 0)
    
    def draw_text_wrapped(self, text, y_position, font, color, max_width=700):
        """Draw wrapped text"""
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if font.size(test_line)[0] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        for i, line in enumerate(lines[:3]):  # Max 3 lines
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, y_position + i * 35))
            self.screen.blit(text_surface, text_rect)
    
    def update(self, is_listening=False, is_speaking=False, status="", command="", response=""):
        """Update GUI"""
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        # Update status
        if status:
            self.status = status
        if command:
            self.command_text = command
        if response:
            self.response_text = response
        
        # Clear screen
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw particles
        self.update_particles()
        for particle in self.particles:
            alpha = int((particle['life'] / 60) * 255)
            color = (*ACCENT_COLOR, alpha)
            pygame.draw.circle(self.screen, ACCENT_COLOR, 
                             (int(particle['x']), int(particle['y'])), 3)
        
        # Draw animated circle
        self.draw_circle_animation(is_listening, is_speaking)
        
        # Draw title
        title = self.title_font.render("J.A.R.V.I.S", True, ACCENT_COLOR)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 50))
        self.screen.blit(title, title_rect)
        
        # Draw status
        status_text = self.small_font.render(self.status, True, TEXT_COLOR)
        status_rect = status_text.get_rect(center=(WINDOW_WIDTH // 2, 120))
        self.screen.blit(status_text, status_rect)
        
        # Draw command
        if self.command_text:
            command_label = self.small_font.render("You:", True, (150, 150, 150))
            self.screen.blit(command_label, (50, 350))
            self.draw_text_wrapped(self.command_text, 380, self.text_font, TEXT_COLOR)
        
        # Draw response
        if self.response_text:
            response_label = self.small_font.render("JARVIS:", True, (150, 150, 150))
            self.screen.blit(response_label, (50, 450))
            self.draw_text_wrapped(self.response_text, 480, self.text_font, ACCENT_COLOR)
        
        # Draw instructions
        instructions = "Say 'Jarvis' to activate | Say 'Exit' to quit"
        inst_text = self.small_font.render(instructions, True, (100, 100, 100))
        inst_rect = inst_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 30))
        self.screen.blit(inst_text, inst_rect)
        
        # Update display
        pygame.display.flip()
        self.clock.tick(60)  # 60 FPS
        
        return True
    
    def cleanup(self):
        """Cleanup GUI resources"""
        pygame.quit()

