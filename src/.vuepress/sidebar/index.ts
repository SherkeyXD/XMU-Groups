import { sidebar } from "vuepress-theme-hope";

export const Sidebar = sidebar({
  "": [
    {
      icon: "discover",
      text: "群列表",
      link: "/groups/",
      prefix: "/groups/",
      collapsible: true,
      children: "structure",
    },
    {
      icon: "note",
      text: "添加新的群信息",
      link: "/contributing/",
      prefix: "/contributing/",
      collapsible: true,
      children: "structure",
    },
  ],
});
