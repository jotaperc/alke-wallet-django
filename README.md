# alke-wallet-django
# Alke Wallet - Sistema de Gestión Financiera (Backend)

Este proyecto es una aplicación web dinámica diseñada para la gestión de usuarios y transacciones financieras, desarrollada bajo la arquitectura **MVT (Model-View-Template)** de Django.

### 🚀 Desafío Técnico
El objetivo principal fue transicionar de una interfaz estática a una plataforma con **persistencia de datos**, garantizando que la información de saldos y registros de usuarios no se perdiera al reiniciar el servidor.

### 🛠️ Solución e Implementación
- **ORM de Django:** Utilizado para gestionar la base de datos SQLite de forma eficiente y segura.
- **CRUD Completo:** Implementación de vistas para crear, leer y listar usuarios en tiempo real.
- **Seguridad:** Uso de middleware de Django y `csrf_token` para la protección de formularios.
- **Frontend:** Interfaz responsiva integrada con **Bootstrap 5**.

### 📊 Métricas de Impacto
- **Integridad de Datos:** 100% de persistencia en registros de transacciones.
- **Eficiencia:** Optimización de consultas al modelo mediante el ORM, reduciendo la carga de lógica en las plantillas.

---
*Proyecto desarrollado como caso de estudio para el Bootcamp de DESARROLLO DE APLICACIONES FULLSTACK PYTHON TRAINEE. SENCE*
