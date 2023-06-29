import requests

response = requests.post("http://localhost:5000/api",json={"input_params":
                                                                                            "compute score for this"})

print(response)
print(response.json())
