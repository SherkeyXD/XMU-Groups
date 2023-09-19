import { navbar } from "vuepress-theme-hope";

export const Navbar = navbar([
  { 
    text: "首页", 
    icon: "bx:home", 
    link: "/" 
  },
  { 
    text: "群列表", 
    icon: "dashicons:groups", 
    link: "/groups/" 
  },
  { 
    text: "添加群信息", 
    icon: "tabler:edit", 
    link: "/contributing/贡献指南.md" 
  },
]);
