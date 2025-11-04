import discord
from WotdHandler import WordHandler


class menuView(discord.ui.View):

    def __init__(self, wotdHandler:WordHandler):
        self.wotdHandler = wotdHandler
        self.optionFunctions = {"option 1" : self.option_1_response,
                                "option 2" : self.option_2_response}
        super().__init__(timeout=60)

    @discord.ui.select(
        placeholder="enter select menu",
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(
                label="option 1",
                description ="description 1"
            ),
            discord.SelectOption(
                label="option 2",
                description ="description 2"
            )
        ]
    )
    async def test_callback(self, interaction:discord.Interaction, select=discord.ui.Select):
        runFun = self.optionFunctions[select.values[0]]
        if runFun:
            await runFun(interaction)
        else:
            await interaction.response.send_message("no function for this option")

    async def option_1_response(self, interaction:discord.Interaction):
        word = self.wotdHandler.run_wotd()
        await interaction.response.send_message(f"Word of the day (TESTING): {word}")
    async def option_2_response(self, interaction:discord.Interaction):
        await interaction.response.send_message("option 2 selected")