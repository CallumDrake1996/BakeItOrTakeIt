from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_ZX6UzidDK1RcWfA7pCW2K86eZ224Fc4BWury")

# Prepare the actor input
run_input = {
    "query": "ASDA Milk Chocolate Chips",
    "limit": 5,
}

# Run the actor and wait for it to finish
run = client.actor("jupri/asda-scraper").call(run_input=run_input)

# Fetch and print actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)