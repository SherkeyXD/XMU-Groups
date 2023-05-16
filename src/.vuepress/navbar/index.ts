import { navbar } from "vuepress-theme-hope";

export const Navbar = navbar([

  { 
    text: "首页", 
    icon: "home", 
    link: "/" 
  },
  { 
    text: "群列表", 
    icon: "discover", 
    link: "/groups/" 
  },
  { 
    text: "贡献指南", 
    icon: "note", 
    link: "/contributing/" 
  },
  {
    text: "V2 文档",
    icon: "note",
    link: "https://theme-hope.vuejs.press/zh/",
  },
]);
