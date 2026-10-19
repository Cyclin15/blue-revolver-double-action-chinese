# -*- coding: utf-8 -*-
"""Build 中文.json for BLUE REVOLVER: DOUBLE ACTION.

Merges our translations over strings/english.json extracted from the game exe.
Entry value forms:
  "str"              -> {"english": <orig>, "中文": "str"}
  {index: "str",...} -> splice into the original list value (keeps colors/numbers)
   (no entry)        -> {"english": <orig>}  (game falls back to English)
"""
import json, re, sys, io

ENG = json.load(open('extracted/strings/english.json', encoding='utf-8'))

# ---------------------------------------------------------------- translations
T = {
# ---- misc / global
"areyousure": "确定吗？",
"back": "返回",
"yes": "是",
"no": "否",
"on": "开",
"off": "关",
"pressanykey": "按任意键",
"continue_prompt": "按 SPECIAL 键继续！",
"rank_level": "等级 %d",
"run_bonus": "单局奖励",

# ---- assist options
"assist_enhancedshot": "强化射击",
"assist_enhancedshot_description": "主武器伤害提升。（+35%）",
"assist_freeplay": "自由模式",
"assist_freeplay_description": "街机式续关：生命耗尽时可以补满生命并继续。",
"assist_infiniteammo": "无限弹药",
"assist_infiniteammo_description": "所有特殊武器弹药无限。",
"assist_reducedbullets": "弹幕削减",
"assist_reducedbullets_description": "需要应对的敌方弹幕减少 50%。",
"assist_slowbullets": "弹幕减速",
"assist_slowbullets_description": "敌方弹幕速度降低 40%。（注意：这不一定能让游戏变简单……）",
"assist_superautobomb": "超级自动炸弹",
"assist_superautobomb_description": "所有模式下都会自动释放炸弹，为你挡下致命一击。超级自动炸弹只消耗一枚炸弹，而不是全部库存。",

# ---- bosses (names/craft kept in English; quotes translated)
"boss1quote": "喂喂喂，开着那种机器，你这是要去哪儿呀？",
"boss1quote_val": "……",
"boss2quote": "那台 Device 似乎没有登记在我们的数据库里。是有人把它转卖给你的吗？",
"boss2quote_val": "……",
"boss3quote": "这猫捉老鼠的游戏我已经玩腻了。能不能麻烦你自己去自首？",
"boss3quote_val": "看到你到头来还是安然无恙，我就放心了。",
"boss4quote": "你的事迹我早有耳闻。从那台机体里出来，陪我玩玩吧！",
"boss4quote_val": "哟嚯！！你知道我的机体飞到哪儿去了吗？",
"boss5quote": "如果我现在不出手，我们俩可能就都要完蛋了。希望你已经准备好了。",
"boss5quote_val": "你不能永远都沉浸在这样的梦里。",
"boss6quote": "并不是只有你一个人会打破规则。",
"boss7name": "???",

# ---- credits (headers translated, names kept)
"credits_1": {0: "=制作人员="},
"credits_2": {0: "设计 / 程序"},
"credits_3": {0: "美术指导"},
"credits_4": {0: "背景美术"},
"credits_5": {0: "音乐"},
"credits_6": {0: "音效"},
"credits_7": {0: "=客座嘉宾="},
"credits_8": {0: "配音"},
"credits_9": {0: "母带处理"},
"credits_10": {0: "音乐混音"},
"credits_11": {0: "客座画廊"},
"credits_12": {0: "本地化"},
"credits_13": {0: "测试人员"},
"credits_14": {0: "=星际玩家=", 2: "=世界纪录保持者=", 4: "=完美平行通关="},
"credits_15": {0: "=v0.5 分数挑战="},
"credits_16": {0: "基于 LOVE 引擎构建", 3: "=程序库=", 12: "=字体="},
"credits_17": {3: "呈现："},
"credits_thanks": ["感谢游玩。"],
"credits_thanks_hyper": ["感谢游玩。", "", "试试平行模式吧！"],
"credits_thanks_normal": ["感谢游玩。", "", "试试狂热模式吧！"],
"credits_thanks_parallel": [
    "恭喜通关，并致以发自心底的感谢。",
    "",
    "我们倾注在这款游戏里的时间、煎熬与爱，如果没有像你这样的玩家，便都将归于虚无。",
    "",
    "唯有我们的努力与你们的付出相遇，才能创造出真正闪耀的东西。",
    "",
    "愿我们继续并肩前行，愿 STG 永不消亡！",
],

# ---- endings
"dee_ending_1": "DEE：唔……这个模拟训练有哪里不太对劲。",
"dee_ending_2": "DEE：它抛过来的东西我差点就跟不上了。",
"dee_ending_3": "DEE：今天的训练程序是 Ira 负责的。她总不至于擅自改动 Device 的核心设置吧？",
"dee_ending_4": "DEE：我的绩效评分绝对应该更高才对……",
"dee_ending_5": "DEE：……",
"dee_ending_6": "DEE：结束之后我得找她好好谈谈。",
"dee_ending_7": "END",
"mae_ending_1": "MAE：怎么回事？为什么我的 Device 没有反应？",
"mae_ending_2": "DEE（画外音）：那可不是真正的 Device。你可以自认为是创意天才，但显然没有把它真正造出来的本事。",
"mae_ending_3": "DEE（画外音）：我相信其他成员已经提醒过你很多次了——未经许可、缺少正规监管就试图制造这种水平的东西，是违法的。",
"mae_ending_4": "MAE：那你们想让我怎么样嘛！我不想和别人合作，也讨厌陌生人对我指手画脚！",
"mae_ending_5": "DEE：Mae，这件事由不得你任性。",
"mae_ending_6": "DEE：看看你的周围！这里的环境和你 Device 的状态，没有一处是正常的。",
"mae_ending_7": "DEE：更重要的是，你的疏忽大意让所有人的性命都陷入了危险。我们别无选择，只能出手。",
"mae_ending_8": "MAE：所以呢？你是说就因为我做不好，就应该干脆别再造东西了吗？",
"mae_ending_9": "MAE：你们疯了！你们整支队伍都疯了！",
"mae_ending_10": "？？？：住口！她根本不是那个意思！",
"mae_ending_11": "MAE：呜哇！",
"mae_ending_12": "VAL：这是为了安全！我们大老远飞过来，可不是为了践踏你的爱好。这一点你怎么就是不明白呢？！",
"mae_ending_13": "MAE：……",
"mae_ending_14": "MAE：我……我并不是存心想伤害谁……",
"mae_ending_15": "DEE：Val，够了。Mae，如果你愿意听，我可以教你几手高效建造的门道，让你不会再犯同样的错误。",
"mae_ending_16": "DEE：你只要向我们保证，今后不再这样不顾死活地莽撞行事，并且遵守法律。",
"mae_ending_17": "尽管有 Dee 的帮助，Mae 最终还是放弃了野心勃勃的建造计划，转而决定做一名服务于技师们的自由设计师。",
"mae_ending_18": "MAE：行了行了 Dee，你的教导也没白费嘛……你只是让我明白了，把脏活累活丢给别人干，可轻松多了！",
"mae_ending_19": "VAL：倒也是种说法。",
"mae_ending_20": "DEE：我这辈子都没见过这么固执的人……",
"mae_ending_21": "END",
"val_ending_1": "VAL：……",
"val_ending_2": "VAL：我今天要请个病假。",
"val_ending_3": "END",

# ---- difficulty
"difficulty_hyper": "狂热",
"difficulty_normal": "普通",
"difficulty_parallel": "平行",
"difficulty_xmode": "XP 模式",

# ---- errors / leaderboard / replay
"error_leaderboard_upload": "排行榜上传错误。",
"error_replay_attach": "回放附加错误。",
"error_replay_download": "回放下载错误。",
"error_replay_upload": "回放上传错误。",
"leaderboard_ask_retry": "重试？",
"leaderboard_ask_submit": "提交到排行榜？",
"leaderboard_submit_success": "提交成功。",
"leaderboard_submitting": "提交中……",
"leaderboards_download_replay": "下载回放？",
"leaderboards_filter_friends": "好友",
"leaderboards_filter_global": "全球",
"leaderboards_filter_me": "我的分数",
"leaderboards_finished_downloading_replay": "回放下载完成。你可以在回放菜单中找到它。",
"replay_ask_save": "保存回放？",
"replay_framerate_warning": "该回放以高帧率录制，在某些设备上可能会播放缓慢。",
"menu_replay_delete": "删除回放",
"menu_replay_noreplays": "未找到回放。",

# ---- final reward / warnings
"finalreward_congrats": "100% 完成度。\n你已抵达最高点。\n解锁了新的机体配色。",
"finalreward_thanks": "已经没有什么好说的了。\n感谢你一直信赖我们的游戏。\nStellar Circle，2024",
"framerate_warning": "《BLUE REVOLVER》以 60Hz 为设计与测试基准——更改帧率会造成非常细微的手感差异。\n\n排行榜仅支持 60Hz 与 120Hz。",

# ---- intro (colors preserved via splice)
"intro_1": "在这个世界，魔法拥有类似代码的结构。",
"intro_2": "借助科技辅件与脚本编写，使用者得以暂时违逆、改写并操纵自然法则。",
"intro_3": {
    1: "然而，以这种非自然的方式运用魔法，一旦大量使用，便会产生",
    3: "垃圾数据",
    5: "并具象成形——若放任其堆积，将十分危险。",
},
"intro_4": "安全法规强制规定：任何人若未取得执照并接受正规监管，不得制造特定类型的魔法机关。",
"intro_5": {
    1: "一类被称为",
    3: "技师",
    5: "的专家会受训并被派往各地，定期维护并消除各类数据异常。",
},
"intro_6": "最优化的程序与脚本几乎不产生残留，但普通民众使用的大多数脚本都编写得相当拙劣，一旦无人看管，便会催生大量垃圾数据。",
"intro_7": "由于技术要求较高，技师始终供不应求。",
"intro_8": {
    1: "近来，一个名为",
    3: "Blue Revolver",
    5: "的小型技师团体开始崭露头角，他们凭借名为",
    7: "「Device」",
    9: "的高阶工具大放异彩。",
},
"intro_9": "这种魔法遥控器能将复杂、动态的 AI 脚本注入从属机器。",
"intro_10": "仅凭这一件产品，他们的性能与速度便已凌驾于其他同行技师公司之上。",
"intro_11": "据传，目前已知存在的 Device 寥寥无几，且全部登记在 Blue Revolver 名下。",
"intro_12": "然而，深山之中潜伏着一个巨大的数据异常体，其读数与 Device 极为相似。",
"intro_13": "其他技师公司大多对此置若罔闻，以为那不过是 Blue Revolver 的又一造物。",
"intro_14": "为了寻求答案、并期望解除这一异常，Blue Revolver 启程前往调查。",

# ---- main menu
"mainmenu_extras": "附加内容",
"mainmenu_highscores": "最高分",
"mainmenu_missions": "任务",
"mainmenu_options": "设置",
"mainmenu_play": "开始游戏",
"mainmenu_quit": "退出",
"mainmenu_stageselect": "关卡选择",
"mainmenu_unlocks": "解锁内容",
"mainmenu_xmode": "游玩 XP 模式",

# ---- medals
"medal_goal_clear": "通关游戏！",
"medal_goal_clear_parallel": "以平行模式通关！",
"medal_goal_complete": "达成全部目标！",
"medal_goal_score_target": "取得 %s 分并通关！",

# ---- extras menu
"menu_extras_breakguide": "Break 指南",
"menu_extras_completion": "完成度",
"menu_extras_completion_clears": "通关奖章",
"menu_extras_completion_mission_clears": "任务通关",
"menu_extras_completion_mission_medals": "任务奖章",
"menu_extras_completion_parallel_clears": "平行通关奖章",
"menu_extras_completion_score_medals": "分数奖章",
"menu_extras_completion_shop_unlocks": "商店解锁",
"menu_extras_completion_xmode_clears": "XP 模式奖章",
"menu_extras_credits": "制作人员",
"menu_extras_credits_parallel": "制作人员（平行）",
"menu_extras_cutscenes": "过场动画",
"menu_extras_dee_ending": "结局（Dee）",
"menu_extras_gallery": "画廊",
"menu_extras_highscores": "最高分",
"menu_extras_intro": "开场动画",
"menu_extras_leaderboards": "排行榜",
"menu_extras_mae_ending": "结局（Mae）",
"menu_extras_musicroom": "音乐室",
"menu_extras_replays": "回放",
"menu_extras_tutorial_basics": "教程（基础）",
"menu_extras_tutorial_hyper": "教程（狂热）",
"menu_extras_tutorial_scoring": "教程（计分）",
"menu_extras_tutorial_xmode": "教程（XP 模式）",
"menu_extras_tutorials": "教程",
"menu_extras_val_ending": "结局（Val）",
"menu_extras_xmode_ending": "结局（XP 模式）",

# ---- gallery
"menu_gallery_comment_concept1": "被废弃的画廊作品",
"menu_gallery_comment_concept2": "Mae 的初期设计",
"menu_gallery_comment_concept3": "初期主角阵容",
"menu_gallery_comment_concept4": "初期 BOSS 阵容",
"menu_gallery_comment_extra3": "Momobako（播报员 / Mae 配音）",
"menu_gallery_comment_extra4": "Nayuki Yuzu（播报员 / Val 配音）",
"menu_gallery_comment_promo1": "用于 v0.5 版本发布",
"menu_gallery_comment_promo4": "用于 v0.5 高分挑战",
"menu_gallery_credit": "作者：%s",

# ---- music room labels
"menu_music_boss": "BOSS",
"menu_music_challenge": "特殊关卡",
"menu_music_ending": "结局",
"menu_music_finalboss1": "最终BOSS A",
"menu_music_finalboss2": "真BOSS",
"menu_music_interlude": "制作人员",
"menu_music_nameentry": "名字输入",
"menu_music_shipselect": "机体选择",
"menu_music_stage1": "第 1 关",
"menu_music_stage2": "第 2 关",
"menu_music_stage3": "第 3 关",
"menu_music_stage4": "第 4 关",
"menu_music_stage5": "第 5 关",
"menu_music_stagecomplete": "通关",
"menu_music_title": "标题",

# ---- options menu
"menu_options_aghast": "Aghast",
"menu_options_akinola": "Akinola",
"menu_options_all_controllers": "任意",
"menu_options_ammo": "弹药",
"menu_options_announcer": "播报员",
"menu_options_announcervolume": "播报员音量",
"menu_options_apply_display": "应用画面设置",
"menu_options_aspectratio": "画面比例",
"menu_options_audio": "音频",
"menu_options_axis": "轴 %d",
"menu_options_backgroundbrightness": "背景亮度",
"menu_options_backgroundsaturation": "背景饱和度",
"menu_options_bluephoenix": "Blue Phoenix",
"menu_options_bomb": "炸弹",
"menu_options_borderless": "无边框",
"menu_options_bosstheme": "BOSS",
"menu_options_bulletcolors": "弹幕颜色",
"menu_options_bulletcolors_alternate": "替换",
"menu_options_bulletcolors_custom": "自定义",
"menu_options_bulletcolors_custom1blue": "颜色1 蓝",
"menu_options_bulletcolors_custom1green": "颜色1 绿",
"menu_options_bulletcolors_custom1red": "颜色1 红",
"menu_options_bulletcolors_custom2blue": "颜色2 蓝",
"menu_options_bulletcolors_custom2green": "颜色2 绿",
"menu_options_bulletcolors_custom2red": "颜色2 红",
"menu_options_bulletcolors_original": "原版",
"menu_options_bulletglow": "弹幕光晕",
"menu_options_button": "按钮 %d",
"menu_options_cheats": "秘技",
"menu_options_clearshot": "自机子弹透明化",
"menu_options_clockwise": "顺时针",
"menu_options_confirm": "确认",
"menu_options_controller": "手柄",
"menu_options_counterclockwise": "逆时针",
"menu_options_credits": "制作人员",
"menu_options_credits_doubleaction": "作者：Hagane & Exemia",
"menu_options_credits_original": "作者：Qygen",
"menu_options_display": "显示",
"menu_options_down": "下",
"menu_options_downleft": "左下",
"menu_options_downright": "右下",
"menu_options_exemia": "Exemia",
"menu_options_exemia_maddrift": "Exemia+MadDrift",
"menu_options_filter": "滤镜",
"menu_options_fire": "开火",
"menu_options_flashfrequency": "受击闪光频率",
"menu_options_framerate": "帧率",
"menu_options_freeplay": "自由模式",
"menu_options_fullscreen": "全屏",
"menu_options_gadgets": "组件",
"menu_options_gadgets_message": "此功能面向大型高分辨率显示器。",
"menu_options_gameplay": "玩法",
"menu_options_graphics": "画面",
"menu_options_graphicsmode": "模式",
"menu_options_hat": "十字键 %d",
"menu_options_hyphen": "Hyphen",
"menu_options_ikaruga": "ikaruga_nex",
"menu_options_input": "输入",
"menu_options_insane": "强制拉伸",
"menu_options_language": "语言",
"menu_options_lastbosstheme": "最终BOSS",
"menu_options_left": "左",
"menu_options_legibility": "易读性",
"menu_options_mastervolume": "主音量",
"menu_options_menutheme": "菜单",
"menu_options_mitomoro": "Mitomoro",
"menu_options_mixwallpaper": "混合",
"menu_options_momobako": "Mae（CV：Momobako）",
"menu_options_musicvolume": "音乐音量",
"menu_options_nameentrytheme": "名字输入",
"menu_options_nativeratio": "3:4（原生）",
"menu_options_nayuki": "Val（CV：Nayuki Yuzu）",
"menu_options_no_controller": "无",
"menu_options_noannouncer": "无",
"menu_options_norotation": "无",
"menu_options_nowallpaper": "无",
"menu_options_palettes": "配色",
"menu_options_pause": "暂停",
"menu_options_perfect": "整数倍",
"menu_options_proportionate": "等比适配",
"menu_options_qygen": "原版",
"menu_options_rank": "Rank",
"menu_options_rapidfire": "速射",
"menu_options_rebindcontrols": "重新绑定按键",
"menu_options_reduceflashintensity": "减弱闪光强度",
"menu_options_resetachievements": "重置 Steam 成就",
"menu_options_resetconfig": "重置设置",
"menu_options_resetcontrols": "重置按键",
"menu_options_resetsavefile": "重置存档",
"menu_options_resolution": "分辨率",
"menu_options_right": "右",
"menu_options_rotation": "旋转",
"menu_options_rottking": "Rottking",
"menu_options_ruleset": "规则集",
"menu_options_ruleset_classic": "经典",
"menu_options_ruleset_classic_desc": "v1.11 风格的玩法。改变了 Flourish 时机、射击威力、炸弹与计分机制等。与 v1.11 并不完全相同。面向老玩家。",
"menu_options_ruleset_doubleaction": "Double Action",
"menu_options_savefile": "存档",
"menu_options_scaling": "缩放",
"menu_options_scoringinfo": "计分信息",
"menu_options_screen": "屏幕",
"menu_options_showfps": "显示 FPS",
"menu_options_showgadgets": "显示组件",
"menu_options_showhitboxes": "显示判定框",
"menu_options_skipintro": "跳过开场动画",
"menu_options_soundtrack": "配乐",
"menu_options_soundvolume": "音效音量",
"menu_options_special": "特殊",
"menu_options_specialstagetheme": "特殊关卡",
"menu_options_st1theme": "第 1 关",
"menu_options_st2theme": "第 2 关",
"menu_options_st3theme": "第 3 关",
"menu_options_st4theme": "第 4 关",
"menu_options_st5theme": "第 5 关",
"menu_options_terranaut": "Terranaut",
"menu_options_topbar_extend": "奖命",
"menu_options_topbardisplay": "顶栏显示",
"menu_options_transparentscoreitems": "分数道具透明化",
"menu_options_unlockeverything": "解锁全部内容",
"menu_options_up": "上",
"menu_options_upleft": "左上",
"menu_options_upright": "右上",
"menu_options_vsync": "垂直同步",
"menu_options_wallpaper": "壁纸",
"menu_options_wallpapermix1": "壁纸混合 1",
"menu_options_wallpapermix2": "壁纸混合 2",
"menu_options_windowed": "窗口化",

# ---- pause
"pause_quit": "退出",
"pause_restart": "重新开始",
"pause_resume": "继续",
"pause_skip": "跳过",
"pause_title": "回到标题",

# ---- stage select
"menu_stageselect_aftermidboss": "中BOSS之后",
"menu_stageselect_bombs": "炸弹",
"menu_stageselect_lives": "生命",
"menu_stageselect_boss": "BOSS",
"menu_stageselect_character": "角色",
"menu_stageselect_descent": "俯冲",
"menu_stageselect_difficulty": "模式",
"menu_stageselect_freezerank": "固定 Rank",
"menu_stageselect_hypermode": "狂热",
"menu_stageselect_midboss": "中BOSS",
"menu_stageselect_midboss1": "中BOSS 1",
"menu_stageselect_midboss2": "中BOSS 2",
"menu_stageselect_midboss3": "中BOSS 3",
"menu_stageselect_midboss4": "中BOSS 4",
"menu_stageselect_normalmode": "普通",
"menu_stageselect_parallelmode": "平行",
"menu_stageselect_rank": "Rank",
"menu_stageselect_special": "特殊",
"menu_stageselect_stage": "关卡",
"menu_stageselect_stage1": "第 1 关【山地】",
"menu_stageselect_stage2": "第 2 关【港湾】",
"menu_stageselect_stage3": "第 3 关【云海】",
"menu_stageselect_stage4": "第 4 关【基地】",
"menu_stageselect_stage5": "第 5 关【梦境】",
"menu_stageselect_stagestart": "开始",
"menu_stageselect_start": "开始",
"menu_stageselect_startfrom": "起始位置",
"menu_stageselect_truelastboss": "真最终BOSS",
"menu_stageselect_xmode": "XP 模式",

# ---- unlocks menu
"menu_unlocks_filter_description": "「%s」画面滤镜。",
"menu_unlocks_gallery": "画廊\n画作",
"menu_unlocks_gallery_generic_description": "%s 的画作。可用作游戏壁纸。",
"menu_unlocks_need_adjacent": "需要先解锁相邻的项目……",
"menu_unlocks_palette": "Device\n配色",
"menu_unlocks_palette_dee_description": "Dee 的 Device 备用配色。",
"menu_unlocks_palette_mae_description": "Mae 的 Device 备用配色。",
"menu_unlocks_palette_val_description": "Val 的 Device 备用配色。",
"menu_unlocks_presstolisten": "按速射键试听",
"menu_unlocks_remix": "混音\n曲目",
"menu_unlocks_remix_1_description": "菜单曲混音版，作者 Exemia。",
"menu_unlocks_remix_2_description": "第 1 关曲目混音版，作者 Terranaut。",
"menu_unlocks_remix_3_description": "第 1 关曲目混音版，作者 Blue Phoenix。",
"menu_unlocks_remix_4_description": "第 2 关曲目混音版，作者 Mitomoro。",
"menu_unlocks_remix_5_description": "第 2 关曲目混音版，作者 Terranaut。",
"menu_unlocks_remix_6_description": "第 3 关曲目混音版，作者 Exemia。",
"menu_unlocks_remix_7_description": "第 5 关曲目混音版，作者 Hyphen。",
"menu_unlocks_remix_8_description": "BOSS 曲混音版，作者 Exemia 与 MadDrift。",
"menu_unlocks_remix_9_description": "最终BOSS曲混音版，作者 ikaruga_nex。",
"menu_unlocks_remix_10_description": "最终BOSS曲混音版，作者 Aghast。",
"menu_unlocks_remix_11_description": "名字输入曲混音版，作者 Blue Phoenix。",
"menu_unlocks_remix_12_description": "特殊关卡曲混音版，作者 Blue Phoenix。",
"menu_unlocks_remix_13_description": "制作人员曲混音版，作者 Blue Phoenix。",
"menu_unlocks_xweapon_description": "%s。XP 模式使用的特殊武器。（解锁 XP 模式。）",

# ---- missions
"mission_base_name": "基地",
"mission_bossrush_description": "难度很高。与所有 BOSS 轮番交战并取胜！",
"mission_bossrush_name": "BOSS连战",
"mission_breakthrough_description": "在敌军无限的攻势下生存下来。学会躲避自机狙！",
"mission_breakthrough_name": "突破重围",
"mission_clear": "任务完成！",
"mission_clear_target": "通关并达成目标分数！",
"mission_cloud_name": "云海",
"mission_deathbullet_description": "所有敌机被击毁时都会散出弹幕。谨慎走位，通关吧！",
"mission_deathbullet_name": "死亡弹幕",
"mission_dream_name": "梦境",
"mission_experimentalweapon2_description": "你的激光会将弹幕转化为分数，主射击则为激光补充能量。尽情大干一场吧！",
"mission_experimentalweapon2_name": "X-Weapon 2",
"mission_experimentalweapon_description": "你唯一的武器是一件独特的特殊武器。弹药会随时间恢复。通关吧！",
"mission_experimentalweapon_name": "X-Weapon",
"mission_generic_boss_description": "使用指定装备击败 BOSS。",
"mission_generic_stage_description": "使用指定装备通关。",
"mission_harbour_name": "港湾",
"mission_invisiblebullet_description": "弹幕在接近你时会渐渐隐去。通关并击败 BOSS！",
"mission_invisiblebullet_name": "隐形弹幕",
"mission_junkattack_description": "关卡中到处都是塞满弹幕的废铁。小心连锁反应！谨慎挑选要击毁的目标！",
"mission_junkattack_name": "废铁袭击",
"mission_lightninground2_description": "弹速飞快！通关吧！",
"mission_lightninground2_name": "闪电回合 2",
"mission_lightninground_description": "难度很高，且弹速大幅提升。善用炸弹——通关并击败 BOSS！",
"mission_lightninground_name": "闪电回合",
"mission_matador_description": "一枚大型投射物会不停追着你。特殊武器能让它减速。通关吧！",
"mission_matador_name": "斗牛士",
"mission_midbossrush_description": "难度很高。迎战并击败所有中BOSS！",
"mission_midbossrush_name": "中BOSS连战",
"mission_mountain_name": "山地",
"mission_needclears": "再通关 %d 个即可解锁！",
"mission_snakerevenge_description": "稀有敌人再次现身！如何击毁它们将左右难度……",
"mission_snakerevenge_name": "蛇之复仇",
"mission_squibbattle_description": "在被光球追击的同时击败独特的 BOSS！",
"mission_squibbattle_name": "爆竹对决",
"mission_superbomber_description": "你没有特殊武器，但得分会产生炸弹道具。冲击高分吧！",
"mission_superbomber_name": "烈性炸药",
"mission_target": "目标分数！",
"mission_zangyou_description": "迎战并击败独特的超难第 3 关 BOSS！",

# ---- perks
"perk_better_flourish_extension": "Flourish 更容易延长",
"perk_bomb_damages_all": "炸弹能伤害所有敌人",
"perk_dps": "主炮伤害略微提升",
"perk_easier_extends": "更容易奖命",
"perk_extra_bombs": "炸弹掉落更多",
"perk_extra_life": "开局多一条生命",
"perk_focused_dps": "集火射击伤害提升",
"perk_free_refills": "每关补满弹药",
"perk_larger_shots": "自机子弹判定变大",
"perk_longer_counterbomb": "Counterbomb 窗口更长",
"perk_longer_flourish": "Flourish 时间更长",
"perk_more_bomb_ammo": "炸弹产生更多弹药",
"perk_none_classic_ruleset": "经典规则集",
"perk_unfocused_dps": "非集火射击伤害提升",

# ---- ship select
"shipselect_hyper_description": "一如既往的激烈体验。游戏会努力匹配你的实力。适合射击游戏老手。",
"shipselect_normal_description": "面向新手玩家。敌方弹幕更温和，中弹时还会自动释放炸弹。",
"shipselect_parallel_description": "游戏锁定在最高难度。奖命更少，但炸弹更多。如果你能通关这个……",
"shipselect_speed": "移动速度",
"shipselect_speed_fast": "快（100%）",
"shipselect_speed_medium": "中（90%）",
"shipselect_speed_slow": "慢（75%）",
"shipselect_weapon_bit_description": "经典的锁定式武器。只是这激光好像没校准……",
"shipselect_weapon_blast_description": "数量惊人、威力可怜的手雷。",
"shipselect_weapon_cable_description": "这根线缆没有保护层，危险系数爆表。",
"shipselect_weapon_drone_description": "直接命中的伤害少得可怜，还不如打偏。",
"shipselect_weapon_orb_description": "碰到什么弹什么，包括其他光球。",

# ---- extends / start info
"start_bombtoskip": "炸弹：跳过",
"start_experimentalextends": "奖命分数线：\n每 20,000,000",
"start_hyperextends": "奖命分数线：\n5,000,000\n每 15,000,000",
"start_hyperextends_classic": "奖命分数线：\n5,000,000\n15,000,000\n25,000,000\n50,000,000",
"start_normalextends": "奖命分数线：\n5,000,000\n每 10,000,000",
"start_normalextends_classic": "奖命分数线：\n5,000,000\n10,000,000\n20,000,000\n30,000,000",
"start_parallelextends": "奖命分数线：\n40,000,000\n80,000,000\n120,000,000",
"start_parallelextends_classic": "奖命分数线：\n每 15,000,000",

# ---- tutorials
"tutorial_bl_basics_1": "点按或按住 %s，即可使用弹药无限的主炮机枪。",
"tutorial_bl_basics_2": "点按 %s（或按住 %s）可以在保持全速移动的同时射击。",
"tutorial_bl_basics_3": "按住 %s 会收束弹道并略微提升伤害——同时移动减速，便于精密走位。",
"tutorial_bl_basics_4": "按住 %s 使用特殊武器。会消耗弹药，但威力更强。",
"tutorial_bl_basics_5": "危急时刻，用 %s 释放炸弹——短时间内无敌，并将敌方弹幕转化为弹药。",
"tutorial_bl_basics_6": "只有机体中央的黄色部分会被击中——务必保护好它。",
"tutorial_bl_basics_7": "高分表现会奖励额外生命——更多信息请查看「计分」教程。",
"tutorial_bl_basics_8": "祝你好运！",
"tutorial_bl_hyper_1": "狂热模式采用动态难度（\"Rank\"）系统。顶部的横条代表当前难度。",
"tutorial_bl_hyper_2": "共有五个以颜色区分的难度等级。",
"tutorial_bl_hyper_3": "得分会填充难度条，填满后难度升级。",
"tutorial_bl_hyper_4": "死亡会使难度降级。",
"tutorial_bl_hyper_5": "达到最高难度后，难度最终会自行下降——剩余生命越少，下降越快。",
"tutorial_bl_scoring_1": "用主炮机枪快速连续击毁敌机，可以积累 8 连锁。",
"tutorial_bl_scoring_2": "积满 8 连锁后，使用特殊武器即可触发 \"Flourish\"——用它击毁敌机会不断产生分数道具，直到连锁重置！",
"tutorial_bl_scoring_3": "使用炸弹可以延长连锁和 Flourish。",
"tutorial_bl_scoring_4": "\"Break\" 奖励是完成特殊\"技巧\"后获得的分数加成。",
"tutorial_bl_scoring_5": "想拿到这个奖励，就需要快速连续击毁两翼。",
"tutorial_bl_scoring_6": "留意这些标记，就能知道如何取得 Break。",
"tutorial_bl_scoring_6_break": "击毁这个！",
"tutorial_bl_scoring_6_nobreak": "别击毁这个！",
"tutorial_bl_scoring_7": "达到既定分数线即可获得 \"extend\"（奖命）——一条额外生命！",
"tutorial_xmode_1": "在 XP 模式中，特殊武器会消耗大量弹药，但必定产生 x64 分数道具。",
"tutorial_xmode_2": "使用主射击可以补充弹药。在中近距离时效果更好。",
"tutorial_xmode_3": "得分会升级你的机体，同时提高游戏难度。此模式下难度永远不会下降。",
"tutorial_xmode_4": "得分还会补充炸弹。你只能持有 1 枚炸弹，但它能将敌方弹幕转化为分数，并瞬间回满弹药。",
"tutorial_xmode_5": "由炸弹和部分敌机产生的银色分数道具，不会补充炸弹。",
}


# ---- defensive extras: legacy keys referenced in code but absent from english.json
# (dead code paths in the shipped game; providing them avoids crashes if ever hit)
EXTRA = {
    "assist_info": "辅助选项会影响记录的有效性。按开火或特殊键继续。",
    "mission_st1": "第 1 关",
    "mission_st2": "第 2 关",
    "mission_st3": "第 3 关",
    "mission_st4": "第 4 关",
    "mission_st5": "第 5 关",
    "mission_bossrush": "BOSS连战",
    "mission_midbossrush": "中BOSS连战",
    "scoremultiplier": "x%s",
    "Press key for": "请按下按键：",
    "joypadsupport": "支持手柄操作。",
}

# ------------------------------------------------------------------- build
LANG = "中文"

def check_markers(key, orig, trans):
    o = orig if isinstance(orig, str) else "".join(x for x in orig if isinstance(x, str))
    t = trans if isinstance(trans, str) else "".join(x for x in trans if isinstance(x, str))
    for marker in re.findall(r'%[sd]', o):
        if t.count(marker) < o.count(marker):
            raise SystemExit(f"FORMAT MARKER LOST in {key}: {marker!r} orig={o!r} trans={t!r}")

out = {}
translated = 0
for key, val in ENG.items():
    orig = val['english']
    entry = {"english": orig}
    t = T.get(key)
    if isinstance(t, dict):  # splice into list
        newlist = list(orig)
        for idx, s in t.items():
            assert isinstance(orig[idx], str), f"{key}[{idx}] is not a string slot"
            newlist[idx] = s
        entry[LANG] = newlist
        check_markers(key, orig, newlist)
    elif isinstance(t, list):
        assert len(t) == len(orig), f"{key}: list length mismatch"
        entry[LANG] = t
    elif isinstance(t, str):
        entry[LANG] = t
        check_markers(key, orig, t)
    if LANG in entry:
        translated += 1
    out[key] = entry

for k, v in EXTRA.items():
    assert k not in out, k
    out[k] = {"english": v, LANG: v}

unknown = set(T) - set(ENG)
if unknown:
    raise SystemExit("UNKNOWN KEYS: %s" % sorted(unknown))

with open('中文.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

print(f"OK: {len(out)} entries, {translated} translated, {len(out)-translated} fallback-to-English")

# ------------------------------------------------------------------- verify
# 1) valid JSON round-trip
json.load(open('中文.json', encoding='utf-8'))
# 2) every glyph used must exist in Silver.ttf (main CJK-capable font)
from fontTools.ttLib import TTFont
cmap = TTFont('fonts/Silver.ttf').getBestCmap()
missing = {}
for k, v in out.items():
    texts = []
    if isinstance(v.get(LANG), str):
        texts = [v[LANG]]
    elif isinstance(v.get(LANG), list):
        texts = [x for x in v[LANG] if isinstance(x, str)]
    for s in texts:
        for ch in s:
            if ord(ch) not in cmap:
                missing.setdefault(ch, []).append(k)
if missing:
    print("MISSING GLYPHS in Silver.ttf:")
    for ch, keys in missing.items():
        print(f"  {ch!r} (U+{ord(ch):04X}) in {keys[:3]}")
else:
    print("All glyphs present in Silver.ttf")
