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
