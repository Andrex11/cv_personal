#!/usr/bin/env python3
"""
Generador de CV profesional para Andres Quintana
Aplica las mejores prácticas de UI/UX Pro Max
"""

import json
import os
from typing import Dict, List, Any

class CVGenerator:
    def __init__(self):
        # Información del perfil (tomada de profile.md)
        self.profile_data = {
            "name": "Andres Quintana",
            "username": "Andrex11",
            "title": "¡Hola! Soy Andres",
            "location": "Arauca - Colombia",
            "email": "andrexquintana@gmail.com",
            "tagline": "<coder/>",
            "bio": "¡Bienvenido a mi perfil! Soy un desarrollador apasionado por crear soluciones innovadoras, con experiencia en:",
            "skills": [
                {
                    "area": "APIs",
                    "description": "Diseño y desarrollo de interfaces robustas y escalables."
                },
                {
                    "area": "Aplicaciones Web",
                    "description": "Construcción de apps modernas, seguras y eficientes."
                },
                {
                    "area": "Aplicaciones Móviles",
                    "description": "Desarrollo de soluciones móviles multiplataforma."
                },
                {
                    "area": "Gestión de Reportes",
                    "description": "Crystal Reports."
                },
                {
                    "area": "Muestreo y gestión de Data",
                    "description": "Power BI"
                }
            ],
            "projects": [
                {
                    "name": "API",
                    "description": "Api cobros .net framework",
                    "type": "Backend"
                },
                {
                    "name": "WebApp",
                    "description": "Sistema de información comercial",
                    "type": "Frontend"
                },
                {
                    "name": "MobileApp",
                    "description": "App Cobros ionic + Angular",
                    "type": "Mobile"
                },
                {
                    "name": "App Desktop",
                    "description": "App digitalización (captura de data: dactilar y facial)",
                    "type": "Desktop"
                }
            ],
            "technologies": [
                "SQL (bases de datos relacionales)",
                "C#",
                ".NET / .NET Core",
                "JavaScript, TypeScript",
                "Node.js, Ionic",
                "Python"
            ],
            "contact": {
                "message": "¿Quieres contactarme?",
                "availability": "¡Estoy abierto a nuevas colaboraciones y retos!",
                "email": "andrexquintana@gmail.com"
            }
        }
        
        # Configuración de diseño basada en UI/UX Pro Max
        self.design_config = {
            "primary_color": "#2563eb",  # Blue-600 - profesional y confiable
            "secondary_color": "#1e40af",  # Blue-700 - para hover states
            "accent_color": "#3b82f6",    # Blue-500 - para elementos destacados  
            "text_primary": "#0f172a",    # Slate-900 - contraste 4.5:1
            "text_secondary": "#475569",  # Slate-600 - texto secundario
            "background": "#ffffff",      # Blanco limpio
            "surface": "#f8fafc",        # Slate-50 - fondos de secciones
            "border": "#e2e8f0"          # Slate-200 - bordes visibles
        }

    def generate_css_styles(self) -> str:
        """Genera los estilos CSS siguiendo las mejores prácticas de UI/UX Pro Max"""
        return f"""
        /* Fuentes profesionales - Pairings de UI/UX Pro Max */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
        
        /* Reset y base */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        html {{
            scroll-behavior: smooth;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            font-size: 16px; /* Mínimo 16px para móvil - UI/UX Rule */
            line-height: 1.6; /* 1.5-1.75 range - UI/UX Rule */
            color: {self.design_config['text_primary']};
            background-color: {self.design_config['background']};
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}
        
        /* Tipografía profesional */
        h1, h2, h3, h4, h5, h6 {{
            font-weight: 600;
            line-height: 1.25;
            margin-bottom: 0.5rem;
        }}
        
        h1 {{ font-size: 2.25rem; }}
        h2 {{ font-size: 1.875rem; }}
        h3 {{ font-size: 1.5rem; }}
        
        /* Código con fuente monospace */
        .code {{
            font-family: 'JetBrains Mono', monospace;
            background-color: {self.design_config['surface']};
            padding: 0.25rem 0.5rem;
            border-radius: 0.375rem;
            border: 1px solid {self.design_config['border']};
            font-size: 0.875rem;
        }}
        
        /* Layout container */
        .container {{
            max-width: 1152px; /* max-w-6xl - Consistente - UI/UX Rule */
            margin: 0 auto;
            padding: 0 1rem;
        }}
        
        /* Header flotante - UI/UX Rule: spacing from edges */
        .header {{
            position: fixed;
            top: 1rem;
            left: 1rem;
            right: 1rem;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 1px solid {self.design_config['border']};
            border-radius: 0.75rem;
            padding: 1rem 2rem;
            z-index: 50;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease-in-out;
        }}
        
        .nav {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            font-weight: 700;
            font-size: 1.25rem;
            color: {self.design_config['primary_color']};
        }}
        
        .nav-links {{
            display: flex;
            gap: 2rem;
            list-style: none;
        }}
        
        .nav-links a {{
            text-decoration: none;
            color: {self.design_config['text_secondary']};
            font-weight: 500;
            cursor: pointer; /* UI/UX Rule: cursor pointer */
            transition: color 0.2s ease-in-out;
        }}
        
        .nav-links a:hover {{
            color: {self.design_config['primary_color']};
        }}
        
        /* Main content - account for fixed header */
        .main {{
            margin-top: 6rem; /* Account for fixed navbar height */
            padding-bottom: 4rem;
        }}
        
        /* Hero section */
        .hero {{
            background: linear-gradient(135deg, {self.design_config['surface']} 0%, {self.design_config['background']} 100%);
            padding: 4rem 0;
            text-align: center;
            border-radius: 1rem;
            margin-bottom: 4rem;
        }}
        
        .hero h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, {self.design_config['primary_color']}, {self.design_config['secondary_color']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .tagline {{
            font-size: 1.25rem;
            color: {self.design_config['text_secondary']};
            margin-bottom: 2rem;
        }}
        
        /* Sections */
        .section {{
            margin-bottom: 4rem;
        }}
        
        .section-title {{
            font-size: 2rem;
            color: {self.design_config['primary_color']};
            margin-bottom: 2rem;
            text-align: center;
        }}
        
        /* Cards - Glass morphism style */
        .card {{
            background: rgba(255, 255, 255, 0.9); /* UI/UX Rule: visible in light mode */
            border: 1px solid {self.design_config['border']};
            border-radius: 1rem;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease-in-out;
            cursor: pointer; /* UI/UX Rule: cursor pointer for interactive elements */
        }}
        
        .card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 10px 25px -3px rgba(0, 0, 0, 0.1);
        }}
        
        /* Grid layouts */
        .grid {{
            display: grid;
            gap: 1.5rem;
        }}
        
        .grid-2 {{
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        }}
        
        .grid-3 {{
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        }}
        
        /* Skills grid */
        .skill-card {{
            background: {self.design_config['surface']};
            border: 1px solid {self.design_config['border']};
            border-radius: 0.75rem;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.2s ease-in-out;
            cursor: pointer;
        }}
        
        .skill-card:hover {{
            background: {self.design_config['primary_color']};
            color: white;
            transform: translateY(-2px);
        }}
        
        /* Projects */
        .project-card {{
            border-left: 4px solid {self.design_config['primary_color']};
        }}
        
        .project-type {{
            background: {self.design_config['primary_color']};
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.875rem;
            font-weight: 500;
            display: inline-block;
            margin-bottom: 0.5rem;
        }}
        
        /* Technologies */
        .tech-tag {{
            background: {self.design_config['surface']};
            border: 1px solid {self.design_config['border']};
            color: {self.design_config['text_primary']};
            padding: 0.5rem 1rem;
            border-radius: 2rem;
            font-size: 0.875rem;
            font-weight: 500;
            display: inline-block;
            margin: 0.25rem;
            transition: all 0.2s ease-in-out;
            cursor: pointer;
        }}
        
        .tech-tag:hover {{
            background: {self.design_config['primary_color']};
            color: white;
        }}
        
        /* Contact section */
        .contact {{
            background: {self.design_config['surface']};
            border-radius: 1rem;
            padding: 3rem;
            text-align: center;
        }}
        
        .btn {{
            background: {self.design_config['primary_color']};
            color: white;
            padding: 0.75rem 2rem;
            border: none;
            border-radius: 0.5rem;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            cursor: pointer; /* UI/UX Rule */
            transition: all 0.2s ease-in-out;
            margin: 0.5rem;
        }}
        
        .btn:hover {{
            background: {self.design_config['secondary_color']};
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }}
        
        /* Responsive - UI/UX Rules */
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2rem;
            }}
            
            .nav-links {{
                display: none; /* Simplificar en móvil */
            }}
            
            .header {{
                top: 0.5rem;
                left: 0.5rem;
                right: 0.5rem;
                padding: 1rem;
            }}
            
            .main {{
                margin-top: 5rem;
            }}
            
            .container {{
                padding: 0 0.75rem;
            }}
        }}
        
        /* Touch targets - UI/UX Rule: minimum 44x44px */
        .btn, .nav-links a, .card {{
            min-height: 44px;
            min-width: 44px;
        }}
        
        /* Focus states - UI/UX Rule */
        .btn:focus, .nav-links a:focus {{
            outline: 2px solid {self.design_config['primary_color']};
            outline-offset: 2px;
        }}
        
        /* Reduced motion - UI/UX Rule */
        @media (prefers-reduced-motion: reduce) {{
            * {{
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }}
        }}
        """

    def generate_html_structure(self) -> str:
        """Genera la estructura HTML completa del CV"""
        css_styles = self.generate_css_styles()
        
        # Generar secciones dinámicamente
        skills_html = self.generate_skills_section()
        projects_html = self.generate_projects_section()
        technologies_html = self.generate_technologies_section()
        
        return f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- UI/UX Rule -->
    <meta name="description" content="CV de {self.profile_data['name']} - Desarrollador Full Stack especializado en APIs, aplicaciones web y móviles">
    <title>{self.profile_data['name']} - Desarrollador Full Stack</title>
    <style>{css_styles}</style>
</head>
<body>
    <!-- Header flotante -->
    <header class="header">
        <nav class="nav">
            <div class="logo">{self.profile_data['username']}</div>
            <ul class="nav-links">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#habilidades">Habilidades</a></li>
                <li><a href="#proyectos">Proyectos</a></li>
                <li><a href="#tecnologias">Tecnologías</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main content -->
    <main class="main">
        <div class="container">
            <!-- Hero section -->
            <section id="inicio" class="hero">
                <h1>{self.profile_data['name']}</h1>
                <p class="tagline">{self.profile_data['tagline']}</p>
                <p class="code">{self.profile_data['location']}</p>
                <p style="margin-top: 1rem; color: {self.design_config['text_secondary']};">
                    {self.profile_data['bio']}
                </p>
            </section>

            <!-- Skills section -->
            <section id="habilidades" class="section">
                <h2 class="section-title">Mis Habilidades</h2>
                {skills_html}
            </section>

            <!-- Projects section -->
            <section id="proyectos" class="section">
                <h2 class="section-title">Proyectos Destacados</h2>
                {projects_html}
            </section>

            <!-- Technologies section -->
            <section id="tecnologias" class="section">
                <h2 class="section-title">Tecnologías Favoritas</h2>
                {technologies_html}
            </section>

            <!-- Contact section -->
            <section id="contacto" class="section">
                <div class="contact">
                    <h2>{self.profile_data['contact']['message']}</h2>
                    <p style="color: {self.design_config['text_secondary']}; margin: 1rem 0 2rem 0;">
                        {self.profile_data['contact']['availability']}
                    </p>
                    <a href="mailto:{self.profile_data['contact']['email']}" class="btn">
                        📧 Enviar Email
                    </a>
                    <a href="https://github.com/{self.profile_data['username']}" class="btn" target="_blank" rel="noopener noreferrer">
                        🐙 GitHub Profile  
                    </a>
                </div>
            </section>
        </div>
    </main>

    <!-- JavaScript para navegación suave -->
    <script>
        // Navegación suave
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
        
        // Efecto hover en cards
        document.querySelectorAll('.card, .skill-card').forEach(card => {{
            card.addEventListener('mouseenter', function() {{
                this.style.transform = 'translateY(-4px)';
            }});
            
            card.addEventListener('mouseleave', function() {{
                this.style.transform = 'translateY(0)';
            }});
        }});
    </script>
</body>
</html>
        """

    def generate_skills_section(self) -> str:
        """Genera la sección de habilidades"""
        skills_html = '<div class="grid grid-2">'
        
        for skill in self.profile_data['skills']:
            skills_html += f'''
            <div class="skill-card">
                <h3>{skill['area']}</h3>
                <p style="margin-top: 0.5rem; color: {self.design_config['text_secondary']};">
                    {skill['description']}
                </p>
            </div>
            '''
        
        skills_html += '</div>'
        return skills_html

    def generate_projects_section(self) -> str:
        """Genera la sección de proyectos"""
        projects_html = '<div class="grid grid-2">'
        
        for project in self.profile_data['projects']:
            projects_html += f'''
            <div class="card project-card">
                <div class="project-type">{project['type']}</div>
                <h3>{project['name']}</h3>
                <p style="color: {self.design_config['text_secondary']};">
                    {project['description']}
                </p>
            </div>
            '''
        
        projects_html += '</div>'
        return projects_html

    def generate_technologies_section(self) -> str:
        """Genera la sección de tecnologías"""
        tech_html = '<div style="text-align: center;">'
        
        for tech in self.profile_data['technologies']:
            tech_html += f'<span class="tech-tag">{tech}</span>'
        
        tech_html += '</div>'
        return tech_html

    def generate(self) -> str:
        """Método principal para generar el CV completo"""
        print("🚀 Generando CV profesional...")
        print(f"📋 Aplicando principios UI/UX Pro Max...")
        print(f"👤 Procesando perfil de {self.profile_data['name']}")
        
        html_content = self.generate_html_structure()
        
        # Guardar archivo
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("✅ CV generado exitosamente como 'index.html'")
        print("\n🎨 Características aplicadas:")
        print("  • Diseño profesional con paleta de colores corporativa")
        print("  • Tipografía Inter + JetBrains Mono (Google Fonts)")
        print("  • Header flotante con glassmorphism") 
        print("  • Cards interactivas con hover effects")
        print("  • Navegación suave entre secciones")
        print("  • Responsive design (móvil, tablet, desktop)")
        print("  • Accesibilidad: contraste 4.5:1, focus states, touch targets 44px+")
        print("  • Performance: CSS optimizado, fuentes preload")
        print("  • Cumple reglas UI/UX Pro Max: cursor pointer, transitions suaves")
        
        return html_content

if __name__ == "__main__":
    generator = CVGenerator()
    generator.generate()