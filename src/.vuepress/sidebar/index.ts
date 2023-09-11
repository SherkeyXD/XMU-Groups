import { sidebar } from "vuepress-theme-hope";

export const Sidebar = sidebar({
  "": [
    {
      text: "首页",
      icon: "bx:home",
      link: "/",
    },
    {
      text: "群列表",
      icon: "dashicons:groups",
      link: "/groups/",
      prefix: "/groups/",
      collapsible: true,
      children: "structure",
    },
    {
      text: "添加群信息",
      icon: "tabler:edit",
      link: "/contributing/",
      prefix: "/contributing/",
      collapsible: true,
      children: "structure",
    },
  ],
});
