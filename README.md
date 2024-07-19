# nws-cli

A CLI for fetching human-readable weather data from the NWS. 
The main focus of this project is not for fetching machine-readable
data. There are other projects for that.

This tool lets you add as many locations as you like and fetch
a growing number of types of weather reports for each location.

This is just a couple-day hackathon project while the laundry is 
running, but I could see some future features might include 
templatized reports so you can extend the reports however you 
want without adapting the code.

## Quickstart

Install with

```shell
pip install https://codeberg.org/jakekara/nws-weather-cli.git
# or
pip install git+https://github.com/jakekara/nws-cli.git

# Pssst: I'm going to try to develop this over on codeberg,
# so if you're looking at this on GitHub, check there for
# PRs and stuff.
```

Then run the set up wizard to add at least one location.

```shell
nws wizard
```

Follow the on-screen instructions. When you're done, you can 
list your locations to make sure you have a least one (default):

```shell
nws ls
default
jackson
```

These locations are stored in a file at `~/.nws.weather.config`

which is a simple [ini](https://en.wikipedia.org/wiki/INI_file)
config file that you can edit yourself. Yours might look like
this:

```shell
[default]
latitude = 43.478450279256684
longitude = -110.76005295115242
address = 150 E PEARL AVE, JACKSON, WY, 83001

[jackson]
latitude = 43.478450279256684
longitude = -110.76005295115242
address = 150 E PEARL AVE, JACKSON, WY, 83001
```

## Commands

Now that your environment is set up, you can run commands like
`nws hourly`, `nws detailed` and `nws discussion`. These commands
will use your `default` location, unless you specify a `--location`
argument, like `nws --location jackson hourly.`.

Let's look at some example (truncated) outputs:

### nws hourly
```shell
nws hourly
2024-07-18T18:00:00-04:00: Mostly Cloudy T:80F H:54%
2024-07-18T19:00:00-04:00: Mostly Cloudy T:79F H:54%
2024-07-18T20:00:00-04:00: Partly Cloudy T:77F H:56%
2024-07-18T21:00:00-04:00: Partly Cloudy T:74F H:59%
2024-07-18T22:00:00-04:00: Partly Cloudy T:71F H:63%
2024-07-18T23:00:00-04:00: Mostly Clear T:69F H:68%
2024-07-19T00:00:00-04:00: Mostly Clear T:67F H:73%
2024-07-19T01:00:00-04:00: Mostly Clear T:65F H:75%
2024-07-19T02:00:00-04:00: Clear T:63F H:81%
2024-07-19T03:00:00-04:00: Clear T:61F H:87%
```

```shell
nows --location jackson hourly
2024-07-18T16:00:00-06:00: Mostly Sunny T:87F H:22%
2024-07-18T17:00:00-06:00: Sunny T:87F H:21%
2024-07-18T18:00:00-06:00: Clear T:87F H:21%
2024-07-18T19:00:00-06:00: Mostly Clear T:86F H:22%
2024-07-18T20:00:00-06:00: Partly Cloudy T:80F H:28%
2024-07-18T21:00:00-06:00: Partly Cloudy T:74F H:33%
2024-07-18T22:00:00-06:00: Partly Cloudy T:70F H:35%
2024-07-18T23:00:00-06:00: Partly Cloudy T:67F H:39%
2024-07-19T00:00:00-06:00: Partly Cloudy T:63F H:44%
2024-07-19T01:00:00-06:00: Partly Cloudy T:61F H:48%
```

### nws discussion

```shell
nws --location jackson discussion
Area Forecast Discussion
2024-07-18T23:07:00+00:00
https://api.weather.gov/products/f77fbb6e-0640-4892-bc4a-31a039926ae7

000
FXUS65 KRIW 182307
AFDRIW

Area Forecast Discussion
National Weather Service Riverton WY
```

### nws detailed

```shell
nws --location jackson detailed
Tonight
Mostly clear, with a low around 59. Northwest wind around 6 mph.

Friday
Sunny, with a high near 82. Northwest wind around 6 mph.

Friday Night
Mostly clear, with a low around 59. West wind 1 to 5 mph.
```