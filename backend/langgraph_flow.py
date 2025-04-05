from backend.agents.farmer_advisor import get_farm_advice
from backend.agents.market_researcher import get_market_data
from backend.agents.weather_agent import get_weather_data
from backend.agents.environment_agent import get_soil_data


def run_ai_agents(input_data):
    market_data = input_data.get("market_data", "")
    soil_quality = input_data.get("soil_quality", "")
    weather = input_data.get("weather", "")

    advice = get_farm_advice(market_data, soil_quality, weather)
    return {"advice": advice}

