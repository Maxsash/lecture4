import requests

def main():
    #defining parameters to reduce length of line
    base_url = "http://data.fixer.io/api/latest"
    access_key = 'd84f163bd5d22505eca254b51dc1d5ff'

    base = "EUR"
    other = "EUR"

    res = requests.get(f"{base_url}",
                        params={"access_key": access_key, "base": base, "symbols": other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    
    #read the json data and print
    data = res.json()
    rate = data["rates"]["EUR"]
    print(f"1 EUR is equal to {rate} EUR")

if __name__ == "__main__":
    main()