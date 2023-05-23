# 网页端PR教程

::: info
该教程基于项目 [MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights) 的文档修改而来
:::

## 操作全流程

1. 首先进入 XMU-Groups 主仓库，fork 一份代码 <br>
    ![fork仓库](/assets/screenshot/pr-1.png)
2. 点击 Create Fork <br>
    ![fork仓库](/assets/screenshot/pr-2.png)
3. 接下来来到了你的个人仓库，可以看到标题是 “你的名字/XMU-Groups”，下面一行小字 forked from SherkeyXD/XMU-Groups （复制自 XMU-Groups 主仓库） <br>
    ![你fork的repo](/assets/screenshot/pr-3.png)
4. 找到 `groups.json`，点击文件名 <br>
    ![groups.json](/assets/screenshot/pr-4.png)
5. 打开文件后，直接点击文件右上角的 ✏️ 进行编辑 <br>
    ![修改内容](/assets/screenshot/pr-5.png)
6. 根据 [群信息编写规范](/contributing/编写规范.html#编写-json-文件) 编辑内容
7. 改完了，点击文件右上角的 `Commit changes...`按钮 <br>
    ![提交修改](/assets/screenshot/pr-6.png)
8. 在弹出的界面的 `Commit message` 框内简要写一下你的更改内容，`Extended description` 框内可以写点详细信息也可以不写，最后点击 `Commit changes` 按钮 <br>
    ![编写Commit信息](/assets/screenshot/pr-7.png)
9.  还有第二个文件要改的？改完了发现弄错了想再改改？都没关系！重复上一步即可。
10. 全改好了就可以进行 PR 了！直接点 **个人仓库** 里的 Code 选项卡 <br>
    ![切换至Code选项卡](/assets/screenshot/pr-8.png)
11. 点击 `Contribute` 按钮, 随后点击 `New pull request` 按钮 <br>
    ![发起PR](/assets/screenshot/pr-9.png)
12. 你应该能看到大概长这样的页面，记得检查一下名称 <br>
    ![PR界面](/assets/screenshot/pr-10.png)
13. 下滑页面，你可以看到关于你更改内容的直观演示，最后检查一遍更改内容是否正确 <br>
    ![diff演示](/assets/screenshot/pr-11.png)
14. 上滑页面，点击 `Create pull request` 按钮，创建 PR <br>
    ![PR界面](/assets/screenshot/pr-10.png)
15. 等待 PR 被合并就可以啦~
16. 如果还要进行修改的话，回到 **你的个人仓库**，重复 步骤 4-7 即可！<br>
  注意不需要重新 fork 仓库，也不需要操作重新发起 Pull Request，你当前的 Pull Request 仍处于待审核状态，后续的修改会直接进入到这个 Pull Request 中<br>
17.   等审批通过，就全部完成啦！此后你的 GitHub 头像将会自动进入到贡献者列表名单中，非常感谢各位的无私奉献！<br>
