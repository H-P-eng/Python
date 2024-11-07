import sherlock

username = "<karimidriss>"

# Run Sherlock
results = sherlock.sherlock(username)

# Print the results
for platform, link in results.items():
    print(f"Platform: {platform}")
    print(f"Link: {link}")
