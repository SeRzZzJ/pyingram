from pyongram.session.sessions import MemorySession
from pyongram.telegram.methods.telegram_bot_api import TelegramBotApi
from pyongram.utils.update_parser import UpdateParser


class Context:
    def __init__(self, update, bot: TelegramBotApi, session: MemorySession):
        self._update = update
        self._update_parser = UpdateParser(self._update)
        self._bot = bot
        self._session = session

    def __repr__(self):
        return (f"{self.__class__.__name__}(self._update={self._update}, "
                f"self._bot={self._bot}, "
                f"self._session={self._session})")

    @property
    def update(self):
        return self._update

    @property
    def bot(self):
        return self._bot

    @property
    def session(self) -> MemorySession:
        return self._session

    def enter(self, name):
        self._session.label = name

    def exit(self):
        self._session.label = ""

    async def reply(self,
                    text,
                    *,
                    chat_id=None,
                    message_thread_id=None,
                    parse_mode=None,
                    entities=None,
                    disable_web_page_preview=None,
                    disable_notification=None,
                    protect_content=None,
                    reply_parameters=None,
                    reply_markup=None):
        return await self._bot.send_message(self._is_none(chat_id),
                                            text,
                                            message_thread_id,
                                            parse_mode,
                                            entities,
                                            disable_web_page_preview,
                                            disable_notification,
                                            protect_content,
                                            reply_parameters,
                                            reply_markup
                                            )

    def _is_none(self, is_none_value):
        if is_none_value is None:
            return self._update_parser.update_from_id()
        else:
            return is_none_value

    async def forward_message(self,
                              chat_id,
                              from_chat_id,
                              message_thread_id=None,
                              disable_notification=None,
                              protect_content=None,
                              message_id=None):
        return await self._bot.forward_message(self._is_none(chat_id),
                                               from_chat_id,
                                               message_thread_id,
                                               disable_notification,
                                               protect_content,
                                               message_id)

    async def copy_message(
            self,
            from_chat_id,
            message_id,
            *,
            chat_id=None,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.copy_message(self._is_none(chat_id),
                                            from_chat_id,
                                            message_id,
                                            message_thread_id,
                                            caption,
                                            parse_mode,
                                            caption_entities,
                                            disable_notification,
                                            protect_content,
                                            reply_parameters,
                                            reply_markup)

    async def reply_with_photo(
            self,
            photo,
            *,
            chat_id=None,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            has_spoiler=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return self._bot.send_photo(self._is_none(chat_id),
                                    photo,
                                    message_thread_id,
                                    caption,
                                    parse_mode,
                                    caption_entities,
                                    has_spoiler,
                                    disable_notification,
                                    protect_content,
                                    reply_parameters,
                                    reply_markup)

    async def reply_with_media_group(
            self,
            media,
            *,
            chat_id=None,
            message_thread_id=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None):
        return await self._bot.send_media_group(self._is_none(chat_id),
                                                media,
                                                message_thread_id,
                                                disable_notification,
                                                protect_content,
                                                reply_parameters)

    async def reply_with_audio(
            self,
            chat_id,
            audio,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            duration=None,
            performer=None,
            title=None,
            thumbnail=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_audio(self._is_none(chat_id),
                                          audio,
                                          message_thread_id,
                                          caption,
                                          parse_mode,
                                          caption_entities,
                                          duration,
                                          performer,
                                          title,
                                          thumbnail,
                                          disable_notification,
                                          protect_content,
                                          reply_parameters,
                                          reply_markup)

    async def reply_with_dice(
            self,
            emoji=None,
            *,
            chat_id=None,
            message_thread_id=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_dice(self._is_none(chat_id),
                                         emoji,
                                         message_thread_id,
                                         disable_notification,
                                         protect_content,
                                         reply_parameters,
                                         reply_markup)

    async def reply_with_document(
            self,
            document,
            *,
            chat_id=None,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            thumbnail=None,
            disable_notification=None,
            disable_content_type_detection=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_document(self._is_none(chat_id),
                                             document,
                                             message_thread_id,
                                             caption,
                                             parse_mode,
                                             caption_entities,
                                             thumbnail,
                                             disable_notification,
                                             disable_content_type_detection,
                                             protect_content,
                                             reply_parameters,
                                             reply_markup)

    async def reply_with_sticker(self,
                                 chat_id,
                                 sticker,
                                 *,
                                 message_thread_id=None,
                                 emoji=None,
                                 disable_notification=None,
                                 protect_content=None,
                                 reply_parameters=None,
                                 reply_markup=None):
        return await self._bot.send_sticker(self._is_none(chat_id),
                                            sticker,
                                            message_thread_id,
                                            emoji,
                                            disable_notification,
                                            protect_content,
                                            reply_parameters,
                                            reply_markup)

    async def reply_with_video(
            self,
            video,
            *,
            chat_id=None,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            duration=None,
            width=None,
            height=None,
            thumbnail=None,
            has_spoiler=None,
            supports_streaming=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_video(self._is_none(chat_id),
                                          video,
                                          message_thread_id,
                                          caption,
                                          parse_mode,
                                          caption_entities,
                                          duration,
                                          width,
                                          height,
                                          thumbnail,
                                          has_spoiler,
                                          supports_streaming,
                                          disable_notification,
                                          protect_content,
                                          reply_parameters,
                                          reply_markup)

    async def reply_with_animation(
            self,
            animation,
            *,
            chat_id=None,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            duration=None,
            width=None,
            height=None,
            thumbnail=None,
            has_spoiler=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_animation(self._is_none(chat_id),
                                              animation,
                                              message_thread_id,
                                              caption,
                                              parse_mode,
                                              caption_entities,
                                              duration,
                                              width,
                                              height,
                                              thumbnail,
                                              has_spoiler,
                                              disable_notification,
                                              protect_content,
                                              reply_parameters,
                                              reply_markup)

    async def reply_with_video_note(
            self,
            video_note,
            *,
            chat_id=None,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            duration=None,
            length=None,
            thumbnail=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_video_note(self._is_none(chat_id),
                                               video_note,
                                               message_thread_id,
                                               caption,
                                               parse_mode,
                                               caption_entities,
                                               duration,
                                               length,
                                               thumbnail,
                                               disable_notification,
                                               protect_content,
                                               reply_parameters,
                                               reply_markup)

    async def reply_with_invoice(self,
                                 chat_id,
                                 title,
                                 description,
                                 payload,
                                 provider_token,
                                 currency,
                                 prices,
                                 *,
                                 message_thread_id=None,
                                 max_tip_amount=None,
                                 suggested_tip_amounts=None,
                                 start_parameter=None,
                                 provider_data=None,
                                 photo_url=None,
                                 photo_size=None,
                                 photo_width=None,
                                 photo_height=None,
                                 need_name=None,
                                 need_phone_number=None,
                                 need_email=None,
                                 need_shipping_address=None,
                                 send_phone_number_to_provider=None,
                                 send_email_to_provider=None,
                                 is_flexible=None,
                                 disable_notification=None,
                                 protect_content=None,
                                 reply_parameters=None,
                                 reply_markup=None
                                 ):
        return await self._bot.send_invoice(self._is_none(chat_id),
                                            title,
                                            description,
                                            payload,
                                            provider_token,
                                            currency,
                                            prices,
                                            message_thread_id,
                                            max_tip_amount,
                                            suggested_tip_amounts,
                                            start_parameter,
                                            provider_data,
                                            photo_url,
                                            photo_size,
                                            photo_width,
                                            photo_height,
                                            need_name,
                                            need_phone_number,
                                            need_email,
                                            need_shipping_address,
                                            send_phone_number_to_provider,
                                            send_email_to_provider,
                                            is_flexible,
                                            disable_notification,
                                            protect_content,
                                            reply_parameters,
                                            reply_markup)

    async def reply_with_game(self,
                              chat_id,
                              game_short_name,
                              message_thread_id=None,
                              disable_notification=None,
                              protect_content=None,
                              reply_parameters=None,
                              reply_markup=None):
        return await self._bot.send_game(self._is_none(chat_id),
                                         game_short_name,
                                         message_thread_id,
                                         disable_notification,
                                         protect_content,
                                         reply_parameters,
                                         reply_markup)

    async def reply_with_voice(
            self,
            voice,
            *,
            chat_id=None,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            duration=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_voice(self._is_none(chat_id),
                                          voice,
                                          message_thread_id,
                                          caption,
                                          parse_mode,
                                          caption_entities,
                                          duration,
                                          disable_notification,
                                          protect_content,
                                          reply_parameters,
                                          reply_markup)

    async def reply_with_poll(
            self,
            question,
            options,
            *,
            chat_id=None,
            message_thread_id=None,
            is_anonymous=None,
            poll_type=None,
            allows_multiple_answers=None,
            correct_option_id=None,
            explanation=None,
            explanation_parse_mode=None,
            explanation_entities=None,
            open_period=None,
            close_date=None,
            is_closed=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_poll(self._is_none(chat_id),
                                         question,
                                         options,
                                         message_thread_id,
                                         is_anonymous,
                                         poll_type,
                                         allows_multiple_answers,
                                         correct_option_id,
                                         explanation,
                                         explanation_parse_mode,
                                         explanation_entities,
                                         open_period,
                                         close_date,
                                         is_closed,
                                         disable_notification,
                                         protect_content,
                                         reply_parameters,
                                         reply_markup)

    async def reply_with_quiz(
            self,
            question,
            options,
            *,
            chat_id=None,
            message_thread_id=None,
            is_anonymous=None,
            poll_type=None,
            allows_multiple_answers=None,
            correct_option_id=None,
            explanation=None,
            explanation_parse_mode=None,
            explanation_entities=None,
            open_period=None,
            close_date=None,
            is_closed=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_poll(self._is_none(chat_id),
                                         question,
                                         options,
                                         message_thread_id,
                                         is_anonymous,
                                         poll_type if poll_type else "quiz",
                                         allows_multiple_answers,
                                         correct_option_id,
                                         explanation,
                                         explanation_parse_mode,
                                         explanation_entities,
                                         open_period,
                                         close_date,
                                         is_closed,
                                         disable_notification,
                                         protect_content,
                                         reply_parameters,
                                         reply_markup)

    async def reply_with_chat_action(
            self,
            action,
            *,
            chat_id=None,
            message_thread_id=None):
        return await self._bot.send_chat_action(self._is_none(chat_id),
                                                action,
                                                message_thread_id)

    async def reply_with_location(
            self,
            latitude,
            longitude,
            *,
            chat_id=None,
            message_thread_id=None,
            proximity_alert_radius=None,
            heading=None,
            live_period=None,
            horizontal_accuracy=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_location(self._is_none(chat_id),
                                             latitude,
                                             longitude,
                                             message_thread_id,
                                             proximity_alert_radius,
                                             heading,
                                             live_period,
                                             horizontal_accuracy,
                                             disable_notification,
                                             protect_content,
                                             reply_parameters,
                                             reply_markup)

    async def reply_with_venue(
            self,
            latitude,
            longitude,
            title,
            address,
            *,
            chat_id=None,
            message_thread_id=None,
            foursquare_id=None,
            foursquare_type=None,
            google_place_id=None,
            google_place_type=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_venue(self._is_none(chat_id),
                                          latitude,
                                          longitude,
                                          title,
                                          address,
                                          message_thread_id,
                                          foursquare_id,
                                          foursquare_type,
                                          google_place_id,
                                          google_place_type,
                                          disable_notification,
                                          protect_content,
                                          reply_parameters,
                                          reply_markup)

    async def reply_with_contact(
            self,
            phone_number,
            first_name,
            *,
            chat_id=None,
            message_thread_id=None,
            last_name=None,
            vcard=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None):
        return await self._bot.send_contact(self._is_none(chat_id),
                                            phone_number,
                                            first_name,
                                            message_thread_id,
                                            last_name,
                                            vcard,
                                            disable_notification,
                                            protect_content,
                                            reply_parameters,
                                            reply_markup)

    async def reply_with_markdown(self,
                                  text,
                                  *,
                                  chat_id=None,
                                  message_thread_id=None,
                                  parse_mode=None,
                                  entities=None,
                                  disable_web_page_preview=None,
                                  disable_notification=None,
                                  protect_content=None,
                                  reply_parameters=None,
                                  reply_markup=None):
        return await self._bot.send_message(self._is_none(chat_id),
                                            text,
                                            message_thread_id,
                                            parse_mode if parse_mode else "Markdown",
                                            entities,
                                            disable_web_page_preview,
                                            disable_notification,
                                            protect_content,
                                            reply_parameters,
                                            reply_markup)

    async def reply_with_markdown_v2(self,
                                     text,
                                     *,
                                     chat_id=None,
                                     message_thread_id=None,
                                     parse_mode=None,
                                     entities=None,
                                     disable_web_page_preview=None,
                                     disable_notification=None,
                                     protect_content=None,
                                     reply_parameters=None,
                                     reply_markup=None):
        return await self._bot.send_message(self._is_none(chat_id),
                                            text,
                                            message_thread_id,
                                            parse_mode if parse_mode else "MarkdownV2",
                                            entities,
                                            disable_web_page_preview,
                                            disable_notification,
                                            protect_content,
                                            reply_parameters,
                                            reply_markup)

    async def reply_with_html(self,
                              text,
                              *,
                              chat_id=None,
                              message_thread_id=None,
                              parse_mode=None,
                              entities=None,
                              disable_web_page_preview=None,
                              disable_notification=None,
                              protect_content=None,
                              reply_parameters=None,
                              reply_markup=None):
        return await self._bot.send_message(self._is_none(chat_id),
                                            text,
                                            message_thread_id,
                                            parse_mode if parse_mode else "HTML",
                                            entities,
                                            disable_web_page_preview,
                                            disable_notification,
                                            protect_content,
                                            reply_parameters,
                                            reply_markup)
