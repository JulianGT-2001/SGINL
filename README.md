# Sistema de Inventarios para Negocios Locales

## 📌 Introducción  
Este proyecto es el avance de mi proyecto de grado, cuyo objetivo es desarrollar un sistema de inventarios para negocios locales, construido con **Django**, un framework de desarrollo web en Python. El sistema busca automatizar y optimizar el control de stock, permitiendo a los dueños de negocios gestionar sus inventarios de manera eficiente y precisa.  

El proyecto se basa en la necesidad de herramientas accesibles para pequeños comercios, que no cuenten con recursos tecnológicos avanzados. La solución propuesta integra funcionalidades esenciales como el manejo de productos, categorías, motivos de inventario y tipos de inventarios, todo con una interfaz intuitiva y un diseño visual que refleja la identidad del proyecto.  

---

## 🧰 Tecnologías Usadas  

- **Python 3.11.5**  
  Lenguaje de programación principal, utilizado para desarrollar la lógica del backend del sistema.  

- **Django 5.0**  
  Framework web de alto rendimiento para construir aplicaciones escalables. Proporciona herramientas para manejar modelos de datos, vistas, plantillas y autenticación.  

- **django-admin-interface 0.31.0**  
  Extensión para personalizar la interfaz de administración de Django, permitiendo un diseño visual atractivo y funcional para el panel de administrador.  

- **django-colorfield 0.14.0**  
  Permite la selección de colores en campos de formulario, facilitando la personalización de datos como motivos de inventario o categorías.  

- **Pillow 12.0.0**  
  Biblioteca para manejar imágenes en el sistema, utilizada para procesar y guardar imágenes de productos.  

- **python-slugify 8.0.4**  
  Herramienta para generar URLs amigables a partir de nombres de productos o categorías, mejorando la experiencia del usuario.  

- **sqlparse 0.5.3**  
  Librería para analizar y formatear consultas SQL, útil durante el desarrollo y depuración del sistema.  

- **text-unidecode 1.3**  
  Permite la normalización de caracteres Unicode, asegurando la compatibilidad de datos en diferentes formatos.  

- **tzdata 2025.2**  
  Base de datos de zonas horarias para manejar fechas y tiempos de manera precisa en el sistema.  

---

## 🗄️ Uso de SQLite como Base de Datos  

### **Ventajas de SQLite**  
SQLite es una base de datos relacional de código abierto y de uso gratuito, que se integra directamente con Django. Su uso en este proyecto ofrece las siguientes ventajas:  

1. **Simplicidad y facilidad de uso**:  
   SQLite no requiere un servidor independiente, lo que facilita su configuración y manejo. Solo se necesita un archivo `.sqlite3` para almacenar toda la información del sistema, lo que simplifica el desarrollo y la prueba del proyecto.  

2. **Bajo consumo de recursos**:  
   Al no depender de un servidor externo, SQLite es ideal para proyectos de pequeño a mediano tamaño, como el sistema de inventarios para negocios locales. Es especialmente útil en entornos de desarrollo o en dispositivos con recursos limitados.  

3. **Portabilidad**:  
   La base de datos se almacena en un solo archivo, lo que permite moverla fácilmente entre dispositivos o compartir la base de datos con otros usuarios sin complicaciones.  

4. **Compatibilidad con Django**:  
   Django incluye soporte nativo para SQLite, lo que facilita la integración del sistema de inventarios con la lógica del backend, permitiendo gestionar modelos de datos, consultas y migraciones de manera eficiente.  

5. **Ideal para entornos de desarrollo**:  
   Durante el desarrollo del proyecto, SQLite es una opción excelente para pruebas y prototipado, ya que no requiere configuraciones complejas y permite iterar rápidamente sobre la lógica del sistema.  

---

### **Comodidades del uso de SQLite en este proyecto**  
- **No requiere configuración adicional**:  
  Al usar SQLite, no es necesario configurar un motor de base de datos externo como PostgreSQL o MySQL. Solo se necesita especificar el nombre del archivo en el archivo de configuración (`settings.py`), lo que agiliza el proceso de desarrollo.  

- **Facilita la gestión de datos en entornos locales**:  
  Dado que el sistema está orientado a negocios locales, SQLite permite almacenar y gestionar datos de forma local, sin dependencia de infraestructura externa. Esto es especialmente útil para pequeños comercios que no tienen acceso a servidores dedicados.  

- **Compatibilidad con migraciones Django**:  
  SQLite soporta las migraciones de Django, lo que permite actualizar el esquema de la base de datos de manera segura y automatizada, incluso cuando se modifican modelos de datos.  

- **Ideal para pruebas y despliegue en entornos limitados**:  
  En etapas de desarrollo y prueba, SQLite es una opción económica y eficiente. Además, en entornos donde no se requiere alta escalabilidad, su uso es suficiente para cumplir con las necesidades del sistema.  

---

## 🎯 Propósito y Objetivos  

### **Propósito**  
El sistema se diseñó con el objetivo de ayudar a negocios locales a gestionar sus inventarios de manera eficiente, reduciendo errores humanos y mejorando la precisión en el control de stock.  

### **Objetivos**  
1. **Automatizar el control de inventarios**: Permitir actualizaciones en tiempo real y seguimiento de existencias.  
2. **Facilitar la gestión de datos**: Proporcionar un panel de administración intuitivo para administrar productos, categorías y motivos de inventario.  
3. **Mejorar la experiencia del usuario**: Diseñar una interfaz visual atractiva con tonos morados y amarillos, que reflejen la identidad del proyecto.  
4. **Escalabilidad**: Crear un sistema modular que pueda adaptarse a diferentes tamaños de negocios sin limitaciones.  

---

## 📋 Alcance  

El proyecto se centra en el desarrollo de un sistema de inventarios con las siguientes funcionalidades:  
- **Gestión de productos**: Registro, edición y eliminación de productos, incluyendo imágenes y descripciones.  
- **Categorías**: Organización de productos en categorías para facilitar su búsqueda y manejo.  
- **Motivos de inventario**: Registro de movimientos como entradas, salidas o ajustes de stock.  
- **Tipos de inventarios**: Diferenciación entre inventarios físicos y digitales, o entre diferentes ubicaciones.  

El sistema está orientado a negocios locales, no a empresas de gran escala, lo que lo hace accesible y fácil de usar para usuarios sin experiencia técnica.  

---

## 📌 Conclusión  
Este proyecto representa un esfuerzo para resolver un problema común en el sector de negocios locales: la gestión ineficiente de inventarios. Al integrar tecnologías modernas como Django y una interfaz personalizada, se busca ofrecer una herramienta práctica y escalable.  

El desarrollo del sistema no solo cumple con los requisitos académicos de mi proyecto de grado, sino que también aporta una solución viable para pequeños comercios.  

**Nota:** Este proyecto es el resultado del trabajo de un estudiante universitario. Para consultas o colaboraciones, no duden en contactarme.  
