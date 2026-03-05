# Redis Setup

Redis is used to store surge multiplier values for each zone.

Example:

zone_1 → surge_multiplier = 1.5

Purpose:
- Fast key-value access
- Low latency
- Real-time updates

Testing Commands:

SET surge_test 1.5
GET surge_test

Result:
Redis successfully stores surge multiplier values.