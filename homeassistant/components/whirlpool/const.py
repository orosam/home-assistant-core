"""Constants for the Whirlpool Sixth Sense integration."""

from whirlpool.backendselector import Region

DOMAIN = "whirlpool"

CONF_REGIONS_MAP = {
    "EU": Region.EU,
    "US": Region.US,
}
