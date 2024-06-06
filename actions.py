from nemoguardrails import LLMRails
from nemoguardrails import RailsConfig

config = RailsConfig.from_path("./config")

rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "user",
    "content": "Hello!"
}])
print(response["content"])
