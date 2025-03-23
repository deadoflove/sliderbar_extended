#within

class DragButton(Button):

#search:

		self.eventMove = lambda: None

#Add:

		if app.ENABLE_EXTENDED_SLIDERBAR:
			self.upVisual = None
			self.overVisual = None
			self.downVisual = None

#search:

	def SetMoveEvent(self, event):
		self.eventMove = event

#Add:

	if app.ENABLE_EXTENDED_SLIDERBAR:
		def SetUpVisual(self, filename):
			self.upVisual = filename
			Button.SetUpVisual(self, filename)

		def SetOverVisual(self, filename):
			self.overVisual = filename
			Button.SetOverVisual(self, filename)

		def SetDownVisual(self, filename):
			self.downVisual = filename
			Button.SetDownVisual(self, filename)

#search

	def OnMove(self):
		if self.callbackEnable:
			self.eventMove()

#Add

	if app.ENABLE_EXTENDED_SLIDERBAR:
		def OnMouseOverIn(self):
			if self.overVisual:
				self.SetOverVisual(self.overVisual)

		def OnMouseOverOut(self):
			if self.upVisual:
				self.SetUpVisual(self.upVisual)

		def OnMouseLeftButtonDown(self):
			if self.downVisual:
				self.SetDownVisual(self.downVisual)

		def OnMouseLeftButtonUp(self):
			if self.overVisual:
				self.SetUpVisual(self.overVisual)

#within

class SliderBar(Window):

#search

		self.__CreateCursor()

#Add:

		if app.ENABLE_EXTENDED_SLIDERBAR:
			self.__CreateResetButton()
			self.OnTextButtonReset()


#Search:

		img.LoadImage("d:/ymir work/ui/game/windows/sliderbar.sub")

#replace:

		if app.ENABLE_EXTENDED_SLIDERBAR:
			img.LoadImage("d:/ymir work/ui/game/slider/slidebar01.tga")
		else:
			img.LoadImage("d:/ymir work/ui/game/windows/sliderbar.sub")

#search:

		cursor.SetUpVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")
		cursor.SetOverVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")
		cursor.SetDownVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")

#replace:

		if app.ENABLE_EXTENDED_SLIDERBAR:
			cursor.SetUpVisual("d:/ymir work/ui/game/slider/slidebar_button01.tga")
			cursor.SetOverVisual("d:/ymir work/ui/game/slider/slidebar_button02.tga")
			cursor.SetDownVisual("d:/ymir work/ui/game/slider/slidebar_button01.tga")
		else:
			cursor.SetUpVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")
			cursor.SetOverVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")
			cursor.SetDownVisual("d:/ymir work/ui/game/windows/sliderbar_cursor.sub")

#search:

		self.pageSize = self.backGroundImage.GetWidth() - self.cursor.GetWidth()

#add:

	if app.ENABLE_EXTENDED_SLIDERBAR:
		def __CreateResetButton(self):
			resetButton = Button()
			resetButton.SetParent(self)
			resetButton.SetPosition(self.backGroundImage.GetWidth()-16, 0)
			resetButton.SetUpVisual("d:/ymir work/ui/game/slider/reset01.tga")
			resetButton.SetOverVisual("d:/ymir work/ui/game/slider/reset02.tga")
			resetButton.SetDownVisual("d:/ymir work/ui/game/slider/reset03.tga")
			resetButton.SetEvent(__mem_func__(self.OnReset))
			resetButton.Show()
			self.resetButton = resetButton

		def OnReset(self, pos=0.0):
			self.SetSliderPos(pos)

			if self.eventChange:
				self.eventChange()

		def OnTextButtonReset(self, text="RESET", x=0, y = -19):
			self.resetButton.SetToolTipText(text, x, y)

#search:

	def Enable(self):
		self.cursor.Show()

#add:

		if app.ENABLE_EXTENDED_SLIDERBAR:
			self.resetButton.Show()


#search:

	def Disable(self):
		self.cursor.Hide()

#add:

		if app.ENABLE_EXTENDED_SLIDERBAR:
			self.resetButton.Hide()


