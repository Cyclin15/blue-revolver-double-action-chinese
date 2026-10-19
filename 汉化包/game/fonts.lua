local fonts = {
	-- our pixel fonts
	numbers = love.graphics.newImageFont("data/graphics/font_score.png", "0123456789"),
	numbers_blue = love.graphics.newImageFont("data/graphics/font_score_blue.png", "0123456789"),
	numbers_2x = love.graphics.newImageFont("data/graphics/font_score_2x.png", "0123456789"),
	numbers_3x = love.graphics.newImageFont("data/graphics/font_score_3x.png", "0123456789"),
	numbers_3x_blue = love.graphics.newImageFont("data/graphics/font_score_3x_blue.png", "0123456789"),
	counter = love.graphics.newImageFont("data/graphics/font_counter.png", "0123456789%"),
	green_counter = love.graphics.newImageFont("data/graphics/font_counter2.png", "0123456789%"),
	scoreinfo = love.graphics.newImageFont("data/graphics/font_scoreinfo.png", "+x1234567890"),
	bigfancy = love.graphics.newImageFont("data/graphics/font_letter2_2x.png", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", 2),
	bigselect = love.graphics.newImageFont("data/graphics/font_letter_blue.png", "ABCDEFGHIJKLMNOPQRSTUVWXYZ!", 1),
	fancyenglish = love.graphics.newImageFont("data/graphics/font_letter2.png", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", 1),
	-- basic = love.graphics.newFont("data/graphics/fonts/04b.ttf", 8),
	-- menu = love.graphics.newFont("data/graphics/fonts/88 Zen.ttf", 8),
	fancyrussian = love.graphics.newFont("data/graphics/fonts/FreePixel.ttf", 16),
	english = love.graphics.newFont("data/graphics/fonts/88 Zen.ttf", 8),
	basicenglish = love.graphics.newFont("data/graphics/fonts/04b.ttf", 8),
	japanese = love.graphics.newFont("data/graphics/fonts/PixelMplus10-Regular.ttf", 10), -- love.graphics.newFont("data/graphics/fonts/jackeyfont.ttf", 12),
	basicjapanese = love.graphics.newFont("data/graphics/fonts/misaki_gothic.ttf", 8), -- do we need this?
	basicrussian = love.graphics.newFont("data/graphics/fonts/uni05_53.ttf", 8),
	basiceuro = love.graphics.newFont("data/graphics/fonts/uni05_53.ttf", 8),
	fancyeuro = love.graphics.newFont("data/graphics/fonts/PixelOperator.ttf", 16),
	silver = love.graphics.newFont("data/graphics/fonts/Silver.ttf", 19),
	ikkle = love.graphics.newFont("data/graphics/fonts/ikkle-4.ttf", 4),
	monogram = love.graphics.newFont("data/graphics/fonts/monogram-extended.ttf", 16),
	thaleah = love.graphics.newFont("data/graphics/fonts/ThaleahFat.ttf", 16),
	-- Chinese (userlocs patch): Silver.ttf has full CJK coverage
	chinese = love.graphics.newFont("data/graphics/fonts/Silver.ttf", 10),
	basicchinese = love.graphics.newFont("data/graphics/fonts/Silver.ttf", 10),
	fancychinese = love.graphics.newFont("data/graphics/fonts/Silver.ttf", 16)
}

fonts.bigselect:setLineHeight(1.1)
fonts.silver:setLineHeight(0.7)

fonts.applyLanguage = function()
	if config.values.language == "japanese" then
		fonts.basic = fonts.basicenglish
		fonts.menu = fonts.japanese
		fonts.fancy = fonts.fancyenglish
	elseif config.values.language == "russian" then
		fonts.basic = fonts.basicrussian
		fonts.menu = fonts.english
		fonts.fancy = fonts.fancyrussian
	elseif config.values.language == "中文" then
		fonts.basic = fonts.basicchinese
		fonts.menu = fonts.chinese
		fonts.fancy = fonts.fancychinese
	else
		fonts.basic = fonts.basicenglish
		fonts.menu = fonts.english
		fonts.fancy = fonts.fancyenglish
	end
end

return fonts
