import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

import { searchProPlugin } from "vuepress-plugin-search-pro";

export default defineUserConfig({
  base: "/",

  locales: {
    "/": {
      lang: "zh-CN",
      title: "厦门大学群收集",
      description: "一个收集厦门大学同好群的网站，方便大家寻找组织",
    },
  },

  theme,

  plugins: [
    searchProPlugin({
      indexContent: true,
      hotReload: true,
      hotKeys: [
        { key: "k", ctrl: true }, 
        { key: "f", ctrl: true }, 
      ],
    }),
  ],

  // Enable it with pwa
  // shouldPrefetch: false,
});
