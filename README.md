
# Sistema Experto para Decisiones Financieras

Este proyecto es una implementación básica de un sistema experto para ayudar a tomar decisiones en el sector financiero. Utiliza reglas simples del tipo "si-entonces" para evaluar situaciones financieras y proporcionar recomendaciones.

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

1. `KnowledgeBase.py` - Implementa la base de conocimientos.
2. `Rule.py` - Define las reglas con condiciones y acciones.
3. `ConditionsAndActions.py` - Contiene ejemplos de condiciones y acciones específicas para el dominio financiero.
4. `InferenceEngine.py` - Implementa el motor de inferencia.
5. `Main.py` - Aplicación principal que configura y ejecuta el sistema experto.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/sistema-experto-finanzas.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd sistema-experto-finanzas
    ```

## Uso

### 1. Base de Conocimientos (KnowledgeBase.py)
```python
class KnowledgeBase:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, key, value):
        self.facts[key] = value

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self):
        for rule in self.rules:
            rule.evaluate(self.facts)
```

### 2. Regla (Rule.py)
```python
class Rule:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def evaluate(self, facts):
        if self.condition(facts):
            self.action(facts)
```

### 3. Condiciones y Acciones (ConditionsAndActions.py)
```python
# Ejemplo de condiciones
def condition_high_risk_investment(facts):
    return facts.get('market_volatility') == 'high' and facts.get('investment_type') == 'stocks'

def condition_low_interest_rate(facts):
    return facts.get('interest_rate') < 2.0

def condition_high_inflation(facts):
    return facts.get('inflation_rate') > 3.0

# Ejemplo de acciones
def action_recommend_bonds(facts):
    print("Recomendación: Considerar invertir en bonos debido a la alta volatilidad del mercado.")

def action_recommend_real_estate(facts):
    print("Recomendación: Considerar invertir en bienes raíces debido a las bajas tasas de interés.")

def action_recommend_gold(facts):
    print("Recomendación: Considerar invertir en oro debido a la alta inflación.")
```

### 4. Motor de Inferencia (InferenceEngine.py)
```python
class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def run(self):
        self.knowledge_base.evaluate()
```

### 5. Aplicación Principal (Main.py)
```python
from KnowledgeBase import KnowledgeBase
from Rule import Rule
from ConditionsAndActions import (
    condition_high_risk_investment,
    condition_low_interest_rate,
    condition_high_inflation,
    action_recommend_bonds,
    action_recommend_real_estate,
    action_recommend_gold
)
from InferenceEngine import InferenceEngine

def main():
    # Crear la base de conocimientos
    kb = KnowledgeBase()

    # Añadir hechos a la base de conocimientos
    kb.add_fact('market_volatility', 'high')
    kb.add_fact('investment_type', 'stocks')
    kb.add_fact('interest_rate', 1.5)
    kb.add_fact('inflation_rate', 4.0)

    # Añadir reglas a la base de conocimientos
    rule1 = Rule(condition_high_risk_investment, action_recommend_bonds)
    rule2 = Rule(condition_low_interest_rate, action_recommend_real_estate)
    rule3 = Rule(condition_high_inflation, action_recommend_gold)

    kb.add_rule(rule1)
    kb.add_rule(rule2)
    kb.add_rule(rule3)

    # Crear y ejecutar el motor de inferencia
    engine = InferenceEngine(kb)
    engine.run()

if __name__ == "__main__":
    main()
```

## Ejecución

Para ejecutar la aplicación, asegúrate de estar en el directorio del proyecto y ejecuta:

```bash
python Main.py
```

Esto evaluará las reglas definidas en la base de conocimientos y proporcionará recomendaciones financieras basadas en los hechos ingresados.

## Extensiones y Mejoras

- **Agregar más hechos y reglas:** Puedes extender la base de conocimientos añadiendo más hechos y reglas relevantes para el dominio financiero.
- **Interfaz de usuario:** Implementar una interfaz gráfica o una interfaz web para facilitar la entrada de datos y la visualización de recomendaciones.
- **Subsistema de explicación:** Añadir un subsistema que explique cómo se llegó a una conclusión o recomendación.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, realiza un fork del repositorio y envía un pull request con tus mejoras.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
