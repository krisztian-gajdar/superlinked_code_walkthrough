# **Fullstack Coding Challenge**

Based on [https://github.com/TierMobility/frontend-challenge/tree/feat/fullstack-challange](https://github.com/TierMobility/frontend-challenge/tree/feat/fullstack-challange)

# Instructions

Run using docker-compose.yaml

      docker compose -f "docker-compose.yaml" up -d --build

Frontend: [http://localhost:3000](http://localhost:3000)

Backend [http://localhost:8080](http://localhost:8080/docs)

# Backend details

There are 2 endpoints:

## encode_url

1. takes in one argument url: str
2. cleans url from prefixes
3. validates url
4. Checks if url is already stored
   - returns parsed url if exists
5. using MD5 hashes current time (microsecond accuracy)
6. encodes hash into base62
7. takes first 7 letters (62^7=3.5 trillion possible combination)
8. inserts original url and encoding into database
9. if insert fails retries it with new encoding for 5 seconds until successful
10. returns 'https://tier.app/{encoding}'

## decode_url

1. takes in one argument url: str.
2. cleans url from prefixes
3. validates url
4. Checks if hash is stored
5. returns original url if exists, error otherwise

# Frontend details

I took inspiration from the currency exchange form of the Revolut app. Created 2 way input fields to encode-decode based on input.
Based on the user action different text, and arrow direction is displayed. Input is validated by the backend. CSS is based on tier.app look.

# Ideas for the future

Replace sqlite with document database (e.g. redis) - document DBs scale better in our case because we are not planning to use updates and joins.

Pipeline for building, testing, deploying.

Retention period for urls.

Authentication to protect API for malicious activity.

Implement baseurl/hash redirection based on db values.

Improve performance by caching data based on popularity in given time.

Introduce load balancing solution (clustering, zookeper, etc.)

Having the endpoints on the UI configurable
