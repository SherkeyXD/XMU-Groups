import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

import { searchProPlugin } from "vuepress-plugin-search-pro";

export default defineUserConfig({
  base: "/",

  locales: {
    "/": {
      lang: "zh-CN",
      title: "查查你的",
      description: "一个收集厦门大学同好群的网站，方便大家寻找组织",
    },
  },

  theme,

  plugins: [
    searchProPlugin({
      indexContent: true,
      hotReload: true,
    }),
  ],

  // Enable it with pwa
  // shouldPrefetch: false,
});
