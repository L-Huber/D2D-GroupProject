# This is a webscraption script for get your guide
#it uses the provided list of links to scrape the data from the webpages
import time
import re
import csv
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


driver = webdriver.Firefox()



def webscraping():
    #basic idea from https://pythonbasics.org/selenium-get-html/
    #importing libraries

    link_list = ['https://www.musement.com/us/new-york/9-11-memorial-and-museum-tickets-3515/', 'https://www.musement.com/us/new-york/summit-one-vanderbilt-tickets-355051/', 'https://www.musement.com/us/new-york/nat-geo-day-tour-tastes-and-tales-from-brooklyn-s-little-caribbean-433800/', 'https://www.musement.com/us/new-york/nat-geo-day-tour-the-untold-story-of-central-park-433816/', 'https://www.musement.com/us/new-york/six-flags-great-adventure-admission-tickets-384389/', 'https://www.musement.com/us/new-york/new-york-citypass-r-five-top-attractions-150849/', 'https://www.musement.com/us/new-york/priority-statue-of-liberty-and-ellis-island-reserve-tickets-281800/', 'https://www.musement.com/us/new-york/metropolitan-museum-of-art-self-guided-audio-tour-322058/', 'https://www.musement.com/us/new-york/9-11-ground-zero-walking-tour-with-optional-9-11-museum-and-one-world-observatory-tickets-27970/', 'https://www.musement.com/us/new-york/top-of-the-rock-entrance-tickets-166552/', 'https://www.musement.com/us/new-york/museum-of-modern-art-moma-skip-the-line-tickets-3891/', 'https://www.musement.com/us/new-york/new-york-c3-r-by-citypass-r-147227/', 'https://www.musement.com/us/new-york/six-flags-darien-lake-entrance-tickets-1-422867/', 'https://www.musement.com/us/new-york/the-beast-speedboat-ride-in-new-york-2881/', 'https://www.musement.com/us/new-york/broadway-tickets-to-aladdin-345075/', 'https://www.musement.com/us/new-york/six-flags-hurricane-harbor-new-jersey-admission-tickets-422972/', 'https://www.musement.com/us/new-york/one-world-observatory-tickets-38486/', 'https://www.musement.com/us/new-york/broadway-tickets-to-the-lion-king-345073/', 'https://www.musement.com/us/new-york/best-of-new-york-city-cruise-2737/', 'https://www.musement.com/us/new-york/go-city-new-york-explorer-pass-4902/', 'https://www.musement.com/us/new-york/ground-zero-tour-with-optional-one-world-observatory-ticket-27971/', 'https://www.musement.com/us/new-york/the-museum-of-broadway-entrance-ticket-396053/', 'https://www.musement.com/us/new-york/statue-of-liberty-express-guided-cruise-from-downtown-nyc-266616/', 'https://www.musement.com/us/new-york/new-york-city-landmarks-sightseeing-cruise-with-tour-guide-10168/', 'https://www.musement.com/us/new-york/harbor-lights-cruise-2832/', 'https://www.musement.com/us/new-york/legoland-r-new-york-admission-tickets-2-404114/', 'https://www.musement.com/us/new-york/fotografiska-new-york-admission-tickets-with-drink-option-224835/', 'https://www.musement.com/us/new-york/fast-track-4-hour-statue-of-liberty-and-ellis-island-tour-27965/', 'https://www.musement.com/us/new-york/9-11-memorial-tour-with-priority-entrance-museum-tickets-286121/', 'https://www.musement.com/us/new-york/ground-zero-911-memorial-and-one-world-observatory-upgrade-option-331505/', 'https://www.musement.com/us/new-york/9-11-ground-zero-walking-tour-st-paul-s-chapel-firefighter-s-memorial-wall-and-9-11-memorial-27952/', 'https://www.musement.com/us/new-york/the-new-york-pass-by-go-city-with-100-attractions-24396/', 'https://www.musement.com/us/new-york/the-edge-observation-deck-st-patrick-s-cathedral-and-moma-admission-tickets-347640/', 'https://www.musement.com/us/new-york/broadway-tickets-to-mj-219793/', 'https://www.musement.com/us/new-york/ground-zero-tour-with-optional-ticket-to-9-11-memorial-museum-27969/', 'https://www.musement.com/us/new-york/9-11-memorial-skip-the-line-ticket-and-self-guided-tour-322059/', 'https://www.musement.com/us/new-york/catacombs-by-candlelight-guided-tour-in-new-york-city-349641/', 'https://www.musement.com/us/new-york/import-922-403598/', 'https://www.musement.com/us/new-york/meet-the-met-extended-metropolitan-museum-of-art-tour-286118/', 'https://www.musement.com/us/new-york/nyc-liberty-cruise-2833/', 'https://www.musement.com/us/new-york/trip-to-woodbury-common-premium-outlets-from-nyc-1356/', 'https://www.musement.com/us/new-york/ifly-westchester-indoor-skydiving-279563/', 'https://www.musement.com/us/new-york/statue-of-liberty-and-ellis-island-sunset-cruise-284077/', 'https://www.musement.com/us/new-york/broadway-tickets-to-wicked-345074/', 'https://www.musement.com/us/new-york/broadway-tickets-to-moulin-rouge-the-musical-128896/', 'https://www.musement.com/us/new-york/new-york-city-and-the-high-line-a-self-guided-walking-tour-308356/', 'https://www.musement.com/us/new-york/the-sopranos-sites-bus-tour-24419/', 'https://www.musement.com/us/new-york/statue-of-liberty-ellis-island-and-brooklyn-bridge-happy-hour-cruise-330020/', 'https://www.musement.com/us/new-york/six-flags-the-great-escape-and-hurricane-harbor-admission-tickets-415389/', 'https://www.musement.com/us/new-york/broadway-tickets-to-harry-potter-and-the-cursed-child-120504/', 'https://www.musement.com/us/new-york/wine-tasting-day-trip-from-nyc-128112/', 'https://www.musement.com/us/new-york/superhero-bus-tour-of-nyc-35540/', 'https://www.musement.com/us/new-york/statue-of-liberty-fully-guided-tour-with-ellis-island-356390/', 'https://www.musement.com/us/new-york/american-dream-blacklight-mini-golf-experience-tickets-403331/', 'https://www.musement.com/us/new-york/american-dream-tilt-museum-admission-ticket-403347/', 'https://www.musement.com/us/new-york/gossip-girl-sights-bus-tour-2583/', 'https://www.musement.com/us/new-york/city-sightseeing-hop-on-hop-off-bus-tour-of-uptown-and-downtown-new-york-171339/', 'https://www.musement.com/us/new-york/private-metropolitan-museum-of-art-skip-the-line-guided-tour-277674/', 'https://www.musement.com/us/new-york/central-park-electric-scooter-tour-287689/', 'https://www.musement.com/us/new-york/off-broadway-tickets-to-the-play-that-goes-wrong-348516/', 'https://www.musement.com/us/new-york/lower-manhattan-private-walking-tour-with-ground-zero-and-9-11-museum-392073/', 'https://www.musement.com/us/new-york/broadway-tickets-to-the-book-of-mormon-4218/', 'https://www.musement.com/us/new-york/new-york-city-downtown-sightseeing-cruise-54757/', 'https://www.musement.com/us/new-york/tour-of-greenwich-village-soho-little-italy-and-chinatown-in-french-6685/', 'https://www.musement.com/us/new-york/tickets-to-the-empire-state-building-observatory-at-sunrise-69714/', 'https://www.musement.com/us/new-york/private-best-of-new-york-three-hour-walking-tour-with-photographer-7929/', 'https://www.musement.com/us/new-york/broadway-tickets-to-hamilton-4298/', 'https://www.musement.com/us/new-york/soho-little-italy-chinatown-guided-walking-tour-163570/', 'https://www.musement.com/us/new-york/broadway-tickets-to-chicago-4306/', 'https://www.musement.com/us/new-york/aiany-around-manhattan-architecture-cruise-273726/', 'https://www.musement.com/us/new-york/discover-african-american-culture-tour-in-central-harlem-277152/', 'https://www.musement.com/us/new-york/nyc-chinatown-and-little-italy-guided-food-tour-282559/', 'https://www.musement.com/us/new-york/woodbury-common-premium-outlets-shopping-from-manhattan-24409/', 'https://www.musement.com/us/new-york/big-bus-tour-of-new-york-1-286080/', 'https://www.musement.com/us/new-york/new-york-city-evening-lights-sail-on-the-adirondack-35524/', 'https://www.musement.com/us/new-york/9-11-memorial-tour-with-priority-entrance-observatory-tickets-286120/', 'https://www.musement.com/us/new-york/niagara-falls-day-trip-from-new-york-with-optional-boat-tour-50259/', 'https://www.musement.com/us/new-york/battery-park-and-statue-of-liberty-self-guided-walking-audio-tour-329703/', 'https://www.musement.com/us/new-york/skip-the-line-9-11-memorial-and-museum-with-statue-of-liberty-cruise-330017/', 'https://www.musement.com/us/new-york/chelsea-market-high-line-and-meatpacking-food-history-tour-66017/', 'https://www.musement.com/us/new-york/statue-of-liberty-ellis-island-and-9-11-memorial-pools-guided-tour-330478/', 'https://www.musement.com/us/new-york/new-york-city-financial-district-a-self-guided-audio-tour-332283/', 'https://www.musement.com/us/new-york/new-york-s-gangster-and-mob-guided-walking-tour-349268/', 'https://www.musement.com/us/new-york/american-dream-mirror-maze-ticket-403603/', 'https://www.musement.com/us/new-york/tickets-to-the-empire-state-building-observatory-1-444275/', 'https://www.musement.com/us/new-york/iconic-nyc-architecture-photography-tour-7489/', 'https://www.musement.com/us/new-york/off-broadway-tickets-to-blue-man-group-4351/', 'https://www.musement.com/us/new-york/central-park-full-day-bike-rental-with-picnic-box-5264/', 'https://www.musement.com/us/new-york/one-day-new-york-city-tour-walking-subway-and-ferry-with-optional-one-world-observatory-upgrade-27940/', 'https://www.musement.com/us/new-york/rockefeller-center-guided-tour-167396/', 'https://www.musement.com/us/new-york/skip-the-line-statue-of-liberty-ellis-island-and-battery-park-20389/', 'https://www.musement.com/us/new-york/lady-liberty-60-minute-cruise-214424/', 'https://www.musement.com/us/new-york/two-day-niagara-falls-and-outlet-shopping-excursion-from-nyc-27561/', 'https://www.musement.com/us/new-york/dyker-heights-christmas-wonderland-tour-264824/', 'https://www.musement.com/us/new-york/midtown-manhattan-architecture-and-history-private-walking-tour-275677/', 'https://www.musement.com/us/new-york/2-day-washington-d-c-philadelphia-and-amish-country-tour-from-nyc-27818/', 'https://www.musement.com/us/new-york/harlem-wednesday-service-experience-277156/', 'https://www.musement.com/us/new-york/neighborhoods-of-new-york-tour-brooklyn-bronx-harlem-queens-and-coney-island-50262/', 'https://www.musement.com/us/new-york/liberty-harbor-helicopter-tour-69572/', 'https://www.musement.com/us/new-york/semi-private-metropolitan-museum-of-art-skip-the-line-guided-tour-277671/', 'https://www.musement.com/us/new-york/legoland-r-discovery-center-westchester-tickets-282243/', 'https://www.musement.com/us/new-york/spirit-of-new-jersey-dinner-cruise-326370/', 'https://www.musement.com/us/new-york/ellis-island-statue-and-one-day-double-decker-tour-330458/', 'https://www.musement.com/us/new-york/statue-of-liberty-and-ellis-island-ferry-ticket-optional-upgrade-330472/', 'https://www.musement.com/us/new-york/4-day-niagara-falls-philadelphia-and-amish-country-tour-from-nyc-330674/', 'https://www.musement.com/us/new-york/broadway-2-hour-musical-theatre-guided-tour-in-new-york-348894/', 'https://www.musement.com/us/new-york/bateaux-new-york-dinner-sightseeing-cruise-349100/', 'https://www.musement.com/us/new-york/grand-central-terminal-ny-self-guided-walking-tour-352196/', 'https://www.musement.com/us/new-york/nyc-statue-of-liberty-private-family-tour-358169/', 'https://www.musement.com/us/new-york/nyc-9-11-memorial-and-financial-district-guided-walking-tour-358173/', 'https://www.musement.com/us/new-york/new-york-public-library-self-guided-audio-tour-375604/', 'https://www.musement.com/us/new-york/nyc-official-grand-central-terminal-tour-396160/', 'https://www.musement.com/us/new-york/highlights-of-manhattan-guided-bus-tour-with-ferry-tickets-396238/', 'https://www.musement.com/us/new-york/unique-stories-from-a-9-11-eyewitness-with-a-self-guided-audio-tour-400754/', 'https://www.musement.com/us/new-york/walking-food-tour-through-north-little-italy-400899/', 'https://www.musement.com/us/new-york/broadway-tickets-to-juliet-401263/', 'https://www.musement.com/us/new-york/best-of-manhattan-escorted-5-hour-tour-1354/', 'https://www.musement.com/us/new-york/fourth-of-july-nyc-fireworks-cruise-2967/', 'https://www.musement.com/us/new-york/downtown-nyc-1-day-hop-on-hop-off-bus-tour-1472/', 'https://www.musement.com/us/new-york/sex-and-the-city-hotspots-bus-tour-2588/', 'https://www.musement.com/us/new-york/new-york-city-tv-and-movie-bus-tour-2590/', 'https://www.musement.com/us/new-york/walk-the-old-railway-line-tour-of-highline-chelsea-in-french-6686/', 'https://www.musement.com/us/new-york/harlem-gospel-experience-walking-tour-in-new-york-city-3915/', 'https://www.musement.com/us/new-york/new-york-grand-central-terminal-photo-safari-7441/', 'https://www.musement.com/us/new-york/new-york-city-highlights-bike-tour-5270/', 'https://www.musement.com/us/new-york/new-york-central-park-photo-safari-7455/', 'https://www.musement.com/us/new-york/central-park-guided-bike-tour-with-map-5284/', 'https://www.musement.com/us/new-york/central-park-by-night-photo-safari-7476/', 'https://www.musement.com/us/new-york/new-york-holiday-markets-and-christmas-lights-tour-7006/', 'https://www.musement.com/us/new-york/new-york-city-after-dark-photo-safari-7483/', 'https://www.musement.com/us/new-york/iconic-nyc-sites-photography-tour-7484/', 'https://www.musement.com/us/new-york/private-best-of-new-york-two-hour-walking-tour-with-photographer-7922/', 'https://www.musement.com/us/new-york/world-trade-center-photo-safari-20456/', 'https://www.musement.com/us/new-york/new-york-yankees-home-game-tickets-23056/', 'https://www.musement.com/us/new-york/central-park-tv-and-movie-sites-walking-tour-24398/', 'https://www.musement.com/us/new-york/washington-d-c-day-trip-from-new-york-city-27563/', 'https://www.musement.com/us/new-york/philadelphia-and-amish-countryside-day-tour-from-nyc-27811/', 'https://www.musement.com/us/new-york/day-trip-from-nyc-to-visit-boston-freedom-trail-27816/', 'https://www.musement.com/us/new-york/sailing-trip-to-statue-of-liberty-on-adirondack-31783/', 'https://www.musement.com/us/new-york/new-york-city-evening-lights-sail-on-america-2-0-35526/', 'https://www.musement.com/us/new-york/secrets-of-the-statue-of-liberty-all-inclusive-tour-50033/', 'https://www.musement.com/us/new-york/washington-and-philadelphia-day-trip-from-new-york-50258/', 'https://www.musement.com/us/new-york/off-broadway-tickets-to-the-gazillion-bubble-show-67584/', 'https://www.musement.com/us/new-york/big-city-helicopter-tour-69337/', 'https://www.musement.com/us/new-york/see-30-top-new-york-sights-fun-guide-118086/', 'https://www.musement.com/us/new-york/grand-island-helicopter-tour-69346/', 'https://www.musement.com/us/new-york/broadway-tickets-to-hadestown-120501/', 'https://www.musement.com/us/new-york/lower-east-side-food-tour-84171/', 'https://www.musement.com/us/new-york/pizza-beer-and-history-tour-84176/', 'https://www.musement.com/us/new-york/lobster-and-beer-lovers-sail-aboard-clipper-city-151543/', 'https://www.musement.com/us/new-york/niagara-falls-one-day-tour-from-new-york-city-109517/', 'https://www.musement.com/us/new-york/nyc-limousine-lights-tour-162829/', 'https://www.musement.com/us/new-york/the-high-line-chelsea-guided-walking-tour-163579/', 'https://www.musement.com/us/new-york/greenwich-village-guided-walking-tour-163751/', 'https://www.musement.com/us/new-york/private-or-semi-private-guided-tour-metropolitan-museum-of-art-with-skip-the-line-ticket-109862/', 'https://www.musement.com/us/new-york/broadway-times-square-guided-walking-tour-163765/', 'https://www.musement.com/us/new-york/lower-manhattan-guided-tour-with-optional-access-to-the-statue-of-liberty-164210/', 'https://www.musement.com/us/new-york/nyc-holiday-lights-limousine-tour-164979/', 'https://www.musement.com/us/new-york/secrets-of-hudson-yards-high-line-the-vessel-165676/', 'https://www.musement.com/us/new-york/nyc-pride-walking-tour-175047/', 'https://www.musement.com/us/new-york/tour-noir-a-nyc-sightseeing-theater-experience-214180/', 'https://www.musement.com/us/new-york/broadway-tickets-to-six-220457/', 'https://www.musement.com/us/new-york/famous-artists-of-manhattan-exploration-game-and-tour-230904/', 'https://www.musement.com/us/new-york/1-day-hop-on-hop-off-bus-tour-in-new-york-city-231582/', 'https://www.musement.com/us/new-york/midtown-new-york-tourist-scavenger-hunt-235409/', 'https://www.musement.com/us/new-york/lower-manhattan-tourist-scavenger-hunt-235410/', 'https://www.musement.com/us/new-york/chinatown-street-photography-photo-safari-251052/', 'https://www.musement.com/us/new-york/st-patrick-s-cathedral-skip-the-line-tickets-audio-tour-and-rockefeller-center-walking-tour-251628/', 'https://www.musement.com/us/new-york/harlem-juke-joint-tour-256398/', 'https://www.musement.com/us/new-york/private-jazz-in-nyc-tour-highlights-256791/', 'https://www.musement.com/us/new-york/new-york-city-high-line-and-hudson-yards-walking-tour-264825/', 'https://www.musement.com/us/new-york/day-trip-to-boston-from-new-york-264828/', 'https://www.musement.com/us/new-york/new-york-city-of-contrasts-tour-264829/', 'https://www.musement.com/us/new-york/skyline-tour-of-new-york-city-264832/', 'https://www.musement.com/us/new-york/greenwhich-village-food-and-historic-walking-tour-265473/', 'https://www.musement.com/us/new-york/greenwich-village-food-tour-265474/', 'https://www.musement.com/us/new-york/the-high-line-tour-historic-downtown-and-greenwich-village-food-tour-265479/', 'https://www.musement.com/us/new-york/best-of-nyc-ebike-tour-266620/', 'https://www.musement.com/us/new-york/private-central-park-guided-bike-tour-266922/', 'https://www.musement.com/us/new-york/private-central-park-guided-walking-tour-266925/', 'https://www.musement.com/us/new-york/semi-private-midtown-manhattan-architecture-and-history-walking-tour-275678/', 'https://www.musement.com/us/new-york/lower-manhattan-and-ground-zero-private-walking-tour-275679/', 'https://www.musement.com/us/new-york/semi-private-walking-tour-of-lower-manhattan-and-ground-zero-275680/', 'https://www.musement.com/us/new-york/private-guided-tour-of-the-statue-of-liberty-and-ellis-island-275684/', 'https://www.musement.com/us/new-york/semi-private-guided-tour-statue-of-liberty-and-ellis-island-275685/', 'https://www.musement.com/us/new-york/sugar-hill-north-harlem-tour-277150/', 'https://www.musement.com/us/new-york/harlem-sunday-service-experience-277154/', 'https://www.musement.com/us/new-york/harlem-swing-stroll-and-dance-class-277155/', 'https://www.musement.com/us/new-york/hamilton-heights-sugar-hill-tour-277157/', 'https://www.musement.com/us/new-york/semi-private-central-park-walking-tour-1-277458/', 'https://www.musement.com/us/new-york/private-central-park-walking-tour-1-277459/', 'https://www.musement.com/us/new-york/private-tour-of-the-statue-of-liberty-282408/', 'https://www.musement.com/us/new-york/private-tour-new-york-city-boroughs-brooklyn-the-bronx-harlem-queens-with-coney-island-282409/', 'https://www.musement.com/us/new-york/nyc-financial-district-hamilton-guided-history-tour-282455/', 'https://www.musement.com/us/new-york/4th-of-july-fireworks-sail-from-new-york-282750/', 'https://www.musement.com/us/new-york/shopping-tour-to-woodbury-common-premium-outlets-283470/', 'https://www.musement.com/us/new-york/brownstone-brooklyn-guided-food-tour-284605/', 'https://www.musement.com/us/new-york/new-york-city-e-bike-rentals-288886/', 'https://www.musement.com/us/new-york/new-york-city-midtown-exploration-game-and-tour-301636/', 'https://www.musement.com/us/new-york/new-york-city-self-guided-audio-tour-on-your-phone-303560/', 'https://www.musement.com/us/new-york/new-york-downtown-architecture-self-guided-tour-322060/', 'https://www.musement.com/us/new-york/new-york-alive-after-five-cocktail-cruise-326371/', 'https://www.musement.com/us/new-york/bateaux-new-york-bottomless-mimosa-brunch-cruise-326373/', 'https://www.musement.com/us/new-york/bateaux-statue-of-liberty-lunch-cruise-326374/', 'https://www.musement.com/us/new-york/spirit-of-new-york-dinner-cruise-1-326376/', 'https://www.musement.com/us/new-york/new-york-brunch-cruise-from-pier-61-326378/', 'https://www.musement.com/us/new-york/new-york-brunch-cruise-from-pier-15-326379/', 'https://www.musement.com/us/new-york/tour-de-dia-entero-en-nueva-york-326889/', 'https://www.musement.com/us/new-york/west-village-food-tour-328170/', 'https://www.musement.com/us/new-york/private-day-trip-to-niagara-falls-from-new-york-city-329712/', 'https://www.musement.com/us/new-york/new-york-city-skyline-day-tour-329716/', 'https://www.musement.com/us/new-york/vip-access-911-memorial-and-museum-admission-with-lady-liberty-cruise-330015/', 'https://www.musement.com/us/new-york/new-york-city-tour-pass-330021/', 'https://www.musement.com/us/new-york/vip-access-ellis-island-statue-liberty-and-battery-park-walking-tour-330022/', 'https://www.musement.com/us/new-york/statue-of-liberty-and-ellis-island-guided-french-language-tour-330188/', 'https://www.musement.com/us/new-york/st-patrick-s-cathedral-official-tour-330456/', 'https://www.musement.com/us/new-york/statue-of-liberty-and-ellis-island-tour-in-spanish-330457/', 'https://www.musement.com/us/new-york/911-memorial-museum-and-lady-liberty-cruise-of-nyc-330470/', 'https://www.musement.com/us/new-york/nyc-combo-statue-of-liberty-cruise-st-patrick-s-cathedral-and-dave-and-buster-s-330481/', 'https://www.musement.com/us/new-york/nyc-combo-the-edge-observation-deck-st-patrick-s-cathedral-and-dave-buster-s-330482/', 'https://www.musement.com/us/new-york/guided-tour-of-manhattan-and-summit-one-vanderbilt-tickets-344895/', 'https://www.musement.com/us/new-york/new-york-city-bus-tour-of-brooklyn-bronx-and-queens-346671/', 'https://www.musement.com/us/new-york/from-wall-street-to-the-world-trade-center-walking-tour-347266/', 'https://www.musement.com/us/new-york/brooklyn-bridge-and-dumbo-neighborhood-walking-tour-347270/', 'https://www.musement.com/us/new-york/new-york-city-private-guided-tour-on-subway-347643/', 'https://www.musement.com/us/new-york/new-york-city-holiday-double-decker-bus-and-walking-tour-1-347680/', 'https://www.musement.com/us/new-york/st-patrick-s-cathedral-behind-the-scenes-vip-official-guided-tour-347681/', 'https://www.musement.com/us/new-york/mount-morris-park-historic-walking-tour-with-lunch-1-349263/', 'https://www.musement.com/us/new-york/gleeks-on-broadway-guided-walking-tour-in-new-york-city-349302/', 'https://www.musement.com/us/new-york/harlem-gospel-and-brunch-tour-349321/', 'https://www.musement.com/us/new-york/harlem-jazz-series-2-349322/', 'https://www.musement.com/us/new-york/harlem-renaissance-walking-tour-with-lunch-2-349323/', 'https://www.musement.com/us/new-york/private-influencer-photo-shoot-experience-in-new-york-city-349356/', 'https://www.musement.com/us/new-york/statue-of-liberty-express-ferry-ticket-and-optional-guided-tour-349689/', 'https://www.musement.com/us/new-york/statue-of-liberty-and-st-patrick-s-cathedral-admission-tickets-349691/', 'https://www.musement.com/us/new-york/cocoa-carols-holiday-cruise-in-new-york-350470/', 'https://www.musement.com/us/new-york/nyc-midtown-choose-what-you-like-food-on-foot-tour-351425/', 'https://www.musement.com/us/new-york/central-park-new-york-self-guided-walking-tour-352194/', 'https://www.musement.com/us/new-york/midtown-manhattan-self-guided-walking-tour-352197/', 'https://www.musement.com/us/new-york/wall-street-self-guided-walking-tour-in-new-york-352756/', 'https://www.musement.com/us/new-york/nyc-super-saver-combo-self-guided-tour-of-manhattan-and-brooklyn-352771/', 'https://www.musement.com/us/new-york/new-york-audio-guide-with-travelmate-app-353314/', 'https://www.musement.com/us/new-york/nyc-american-museum-of-natural-history-family-private-tour-356754/', 'https://www.musement.com/us/new-york/nyc-9-11-memorial-wall-street-and-statue-of-liberty-walking-tour-356781/', 'https://www.musement.com/us/new-york/new-york-city-downtown-underground-donut-tour-357044/', 'https://www.musement.com/us/new-york/broadway-behind-the-scenes-tour-366783/', 'https://www.musement.com/us/new-york/big-apple-in-lights-nyc-night-tour-1-369522/', 'https://www.musement.com/us/new-york/discover-nyc-day-tour-with-harbor-cruise-1-377127/', 'https://www.musement.com/us/new-york/new-york-greenwich-village-italian-food-tour-380747/', 'https://www.musement.com/us/new-york/central-park-self-guided-audio-tour-388537/', 'https://www.musement.com/us/new-york/manhattan-central-park-bike-rental-390668/', 'https://www.musement.com/us/new-york/broadway-tickets-to-a-beautiful-noise-the-neil-diamond-musical-392020/', 'https://www.musement.com/us/new-york/statue-of-liberty-and-ellis-island-private-half-day-guided-tour-392074/', 'https://www.musement.com/us/new-york/superheroes-of-new-york-online-exploration-game-397841/', 'https://www.musement.com/us/new-york/entrance-ticket-to-nyc-dueling-pianos-show-397941/', 'https://www.musement.com/us/new-york/history-of-lower-manhattan-self-guided-audio-tour-398542/', 'https://www.musement.com/us/new-york/guggenheim-museum-and-carnegie-hill-tickets-and-audio-tour-398545/', 'https://www.musement.com/us/new-york/the-original-greenwich-village-food-walking-tour-400499/', 'https://www.musement.com/us/new-york/the-darkest-secrets-of-new-york-self-guided-audio-tour-400755/', 'https://www.musement.com/us/new-york/the-heart-and-soul-of-greenwich-village-food-walking-tour-400794/', 'https://www.musement.com/us/new-york/chelsea-market-food-tour-and-visit-to-the-high-line-400915/', 'https://www.musement.com/us/new-york/walking-food-tour-through-chinatown-s-flavors-400926/', 'https://www.musement.com/us/new-york/new-york-luggage-storage-with-2-location-choices-401077/', 'https://www.musement.com/us/new-york/broadway-tickets-to-sweeney-todd-401265/', 'https://www.musement.com/us/new-york/fifth-avenue-audio-guide-walking-tour-with-live-gps-map-404148/', 'https://www.musement.com/us/new-york/soho-chinatown-and-little-italy-audio-guide-walking-tour-app-404268/', 'https://www.musement.com/us/new-york/american-museum-of-natural-history-ticket-and-self-guided-audio-tour-404285/', 'https://www.musement.com/us/new-york/american-dream-s-the-rink-admission-tickets-404503/', 'https://www.musement.com/us/new-york/new-york-architecture-tour-secrets-of-the-skyline-exploration-game-405351/', 'https://www.musement.com/us/new-york/flatiron-district-tour-with-the-city-exploration-game-405365/', 'https://www.musement.com/us/new-york/tour-alexander-hamilton-s-nyc-with-a-self-guided-exploration-game-405381/', 'https://www.musement.com/us/new-york/tour-new-york-s-museum-mile-with-an-exploration-game-app-405383/', 'https://www.musement.com/us/new-york/tour-midtown-new-york-with-mob-hits-hangouts-exploration-game-405385/', 'https://www.musement.com/us/new-york/new-york-soho-district-tour-with-a-city-exploration-game-405399/', 'https://www.musement.com/us/new-york/new-york-upper-west-side-tour-with-a-city-exploration-game-405405/', 'https://www.musement.com/us/new-york/nyc-slavery-and-underground-railroad-walking-tour-409859/', 'https://www.musement.com/us/new-york/new-york-broadway-behind-the-scenes-experience-410519/', 'https://www.musement.com/us/new-york/new-york-brooklyn-bridge-and-dumbo-food-tasting-guided-tour-410522/', 'https://www.musement.com/us/new-york/new-york-broadway-behind-the-scenes-experience-1-410622/', 'https://www.musement.com/us/new-york/nickelodeon-universe-1-day-entrance-ticket-411052/', 'https://www.musement.com/us/new-york/dreamworks-water-park-admission-ticket-411053/', 'https://www.musement.com/us/new-york/new-york-city-boroughs-1-day-pass-426893/', 'https://www.musement.com/us/new-york/city-climb-at-hudson-yards-ticket-426966/', 'https://www.musement.com/us/new-york/new-york-city-boroughs-3-day-pass-429494/', 'https://www.musement.com/us/new-york/new-york-city-boroughs-7-day-pass-429495/', 'https://www.musement.com/us/new-york/new-york-city-boroughs-90-day-pass-429496/', 'https://www.musement.com/us/new-york/new-york-statue-of-liberty-and-ellis-island-tour-by-ferry-429594/', 'https://www.musement.com/us/new-york/lower-east-side-food-and-history-tour-with-tastings-432763/', 'https://www.musement.com/us/new-york/freedom-liberty-cruise-with-views-of-the-statue-of-liberty-434316/', 'https://www.musement.com/us/new-york/rooftop-bar-and-lounge-tour-in-new-york-434358/', 'https://www.musement.com/us/new-york/new-york-private-photography-tour-435987/', 'https://www.musement.com/us/new-york/new-york-lgbtq-greenwich-village-walking-tour-436737/', 'https://www.musement.com/us/new-york/highlights-of-the-metropolitan-museum-of-art-438965/', 'https://www.musement.com/us/new-york/new-york-mets-baseball-game-tickets-at-citi-field-439349/', 'https://www.musement.com/us/new-york/statue-of-liberty-sunset-cruise-445323/', 'https://www.musement.com/us/new-york/private-brooklyn-bridge-guided-bike-tour-266932/', 'https://www.musement.com/us/new-york/private-brooklyn-bridge-guided-walking-tour-267627/', 'https://www.musement.com/us/new-york/brooklyn-bridge-and-dumbo-food-tour-366780/', 'https://www.musement.com/us/new-york/nyc-summer-nights-boat-cruise-with-dj-449315/']
    #ref: for csv: https://www.geeksforgeeks.org/working-csv-files-python/
    #define fields to save data
    fields = ["link", "name", "price", "description", "total_rating", "number_of_ratings"]

    filename = "musement_scraped_data.csv"
    rows = []
    #use index so start by 0
    start_scrape_number = 0
    end_scrape_number = 2
    
    print("Start webscraping now!")

    i = 0
    link_count = str(len(link_list))
    

    #start the iterations of scraping
    for link in link_list:
        driver.get(link)
        #define standard values
        name=""
        price=""
        description=""
        total_rating=""
        number_of_ratings="0"
        
        i = i + 1
        print("scraping page: "+str(i)+"/"+link_count)
        #open website

        #get name
        try:
            name = driver.find_element(By.CLASS_NAME, "src-shared_component-sections-ActivityHeader-title-1qzL").text
            #print(name)
        except:
            pass

        #get price
        time.sleep(1)
        if i == 1:
            cookie_banner = driver.find_element(By.TAG_NAME, "msm-cookie-banner").shadow_root.find_element(By.CSS_SELECTOR, "[data-test=cookie-banner__decline-cookies]")
            cookie_banner.click()
        try:
            time.sleep(1)
            driver.execute_script("document.querySelector('[data-testid=alt-exp-modal-close]')?.click();window.scrollBy(0,600)")
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, "orderbox_1mZlWY_c").click()
            driver.find_element(By.CSS_SELECTOR, "[data-testid=calendar-next-month-button]").click()
            driver.find_element(By.CSS_SELECTOR, "[data-testid=calendar-next-month-button]").click()
            driver.find_element(By.CSS_SELECTOR, "[data-testid=calendar-next-month-button]").click()
            driver.find_elements(By.CSS_SELECTOR, "[data-testid=orderbox_calendar_cell_active_]")[-1].click()
            time.sleep(1)
        except:
            pass
        try:
            driver.execute_script("document.querySelector('.src-shared_component-components-ReadMore-readMore-2Gdu')?.click()")
            time.sleep(1)
        except:
            pass
        try:
            price = driver.find_element(By.CLASS_NAME, "orderbox_2RN3-bU7").text
            #print(price)
        except:
            pass
        try:
            description = driver.find_element(By.CLASS_NAME, "src-shared_component-components-apiHtmlContent-1KaC").text
            #print(description)
        except:
            pass
        try:
            total_rating = driver.find_element(By.CSS_SELECTOR, "span[data-v-14c1e1ed]").text
            #print(total_rating)
            number_of_ratings = driver.find_element(By.CSS_SELECTOR, "a[data-v-14c1e1ed]").text.split(" ")[2]
            #print(number_of_ratings)
        except:
            pass


        #append values to rows
        rows.append([link, name, price, description, total_rating, number_of_ratings])

    #write data to csv after finishing all iterations
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

def wait_random_time():
    time.sleep(random.randint(10, 20))

if __name__ == '__main__':
    webscraping()
