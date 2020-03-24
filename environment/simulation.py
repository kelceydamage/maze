#! /usr/bin/env python
# ------------------------------------------------------------------------ 79->
# Author: ${name=Kelcey Damage}
# Python: 3.5+
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Doc
# ------------------------------------------------------------------------ 79->
"""
This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

"""


# Imports
# ------------------------------------------------------------------------ 79->
import numpy as np


# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class Sun:
    mod = [2.5, 1.3, 0.3, 1.9]

    def __init__(self):
        super().__init__()
        self.annual_sun_map = np.zeros(360)

    @property
    def sun(self):
        return self.annual_sun_map[-1]

    def generate_sun(self, date):
        season = self.seasons[date[2]]
        rate = self.cacluate_seed(
            sigma=self.sigma,
            mean_range=self.mean_range,
            mod=Sun.mod[season],
            days=1
        )
        self.annual_sun_map[self.convert_date_to_index(date)] = 1 + rate

    def get_sun(self, date, historical_window):
        curent_cycle_day = self.convert_date_to_index(date) + 1
        _range = (curent_cycle_day - historical_window, curent_cycle_day)
        return self.annual_sun_map[_range[0]:_range[1]]


class Precipitation:
    mod = [0.8, 2.2, 3.5, 1]

    def __init__(self):
        super().__init__()
        self.annual_precipitation_map = np.zeros(360)
        self.annual_precipitation_decay = np.zeros(360)

    @property
    def precipitation(self):
        return self.annual_precipitation_map[-1]

    def generate_precipitation(self, date):
        season = self.seasons[date[2]]
        #print('SEASON', season, self.convert_date_to_index(date))
        rate = self.cacluate_seed(
            sigma=self.sigma,
            mean_range=self.mean_range,
            mod=Precipitation.mod[season],
            days=1
        )
        self.annual_precipitation_map[self.convert_date_to_index(date)] = 1 + rate

    def generate_precipitation_decay(self, date):
        season = self.seasons[date[2]]
        rate = self.cacluate_seed(
            sigma=self.sigma,
            mean_range=self.mean_range,
            mod=Precipitation.mod[season],
            days=1
        )
        self.annual_precipitation_decay[self.convert_date_to_index(date)] = rate

    def get_precipitation(self, date, historical_window):
        curent_cycle_day = self.convert_date_to_index(date) + 1
        _range = (curent_cycle_day - historical_window, curent_cycle_day)
        #print(date, _range, self.annual_precipitation_map.shape)
        return self.annual_precipitation_map[_range[0]: _range[1]]

    def get_precipitation_decay(self, date, historical_window):
        curent_cycle_day = self.convert_date_to_index(date) + 1
        _range = (curent_cycle_day - historical_window, curent_cycle_day)
        #print(date, _range, self.annual_precipitation_map.shape)
        return self.annual_precipitation_decay[_range[0]: _range[1]]



class Fertility:
    mod = [3.5, 1.1, 0.7, 1.9]

    def __init__(self):
        super().__init__()
        self.annual_fertility_map = np.zeros(360)

    @property
    def fertility(self):
        return self.annual_fertility_map[-1]

    def generate_fertility(self, date):
        season = self.seasons[date[2]]
        rate = self.cacluate_seed(
            sigma=self.sigma,
            mean_range=self.mean_range,
            mod=Fertility.mod[season],
            days=1
        )
        self.annual_fertility_map[self.convert_date_to_index(date)] = 1 + rate

    def get_fertility(self, date, historical_window):
        curent_cycle_day = self.convert_date_to_index(date) + 1
        _range = (curent_cycle_day - historical_window, curent_cycle_day)
        return self.annual_fertility_map[_range[0]:_range[1]]


class EnvironmentalSimulation(Sun, Precipitation, Fertility):

    def __init__(self):
        super().__init__()
        self.sigma = 50
        self.mean_range = [40, 60]
        self.previous_years_average = {
            'sun': [],
            'precipitation': [],
            'fertility': []
        }
        self.seasons = {
            1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2,
            7: 2, 8: 3, 9: 3, 10: 3, 11: 0, 12: 0
        }
        self.generate_fertility((1, 5, 1, 1300))

    def cacluate_seed(self, sigma, mean_range, mod, days):
        def modulated_gaussian(x, mu, sig, mod):
            return (
                1. / (np.sqrt(2. * np.pi) * sig) *
                np.exp(-np.power((x - mu) / sig, 2.) / 2) / mod
            )
        mu = np.random.randint(mean_range[0], mean_range[1])
        normal = np.random.normal(mu, sigma, days)
        return modulated_gaussian(normal, mu, sigma, mod)

    def convert_date_to_index(self, date):
        return (date[2] - 1) * 30 + date[1] - 1

    def roll_over_year(self):
        self.previous_years_average['sun'].append(
            np.mean(self.annual_sun_map)
        )
        self.previous_years_average['precipitation'].append(
            np.mean(self.annual_precipitation_map)
        )
        self.previous_years_average['fertility'].append(
            np.mean(self.annual_fertility_map)
        )
        self.annual_sun_map = np.zeros(360)
        self.annual_precipitation_map = np.zeros(360)
        self.annual_fertility_map = np.zeros(360)






# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
