# -*- coding: utf-8 -*-

# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from selenium.webdriver import Safari

from splinter.driver.webdriver import BaseWebDriver, WebDriverElement
from splinter.driver.webdriver.cookie_manager import CookieManager


class WebDriver(BaseWebDriver):

    driver_name = "Safari"

    def __init__(
        self,
        fullscreen=False,
        wait_time=2,
        **kwargs
    ):

        self.driver = Safari(**kwargs)

        if fullscreen:
            self.driver.execute_script(
                "window.resizeTo(window.screen.width, window.screen.height)"
            )

        self.element_class = WebDriverElement

        self._cookie_manager = CookieManager(self.driver)

        super(WebDriver, self).__init__(wait_time)
