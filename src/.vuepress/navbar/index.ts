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
    text: "添加群信息", 
    icon: "note", 
    link: "/contributing/" 
  },
]);
