from pyongram.network.client import ApiClient
from pyongram.utils.useful_functions import remove_none_value


class TelegramBotApi:
    def __init__(self, token: str):
        self._client = ApiClient(f"https://api.telegram.org/bot{token}")

    def __repr__(self):
        return f"{self.__class__.__name__}(self._client={self._client})"

    async def get_updates(
            self,
            offset,
            limit,
            timeout,
            allowed_updates
    ):
        return await self._client.request_to_api("getUpdates", remove_none_value({
            "offset": offset,
            "limit": limit,
            "timeout": timeout,
            "allowed_updates": allowed_updates
        }))

    async def set_webhook(
            self,
            url,
            certificate=None,
            ip_address=None,
            max_connections=None,
            allowed_updates=None,
            drop_pending_updates=None,
            secret_token=None
    ):
        return await self._client.request_to_api("setWebhook", remove_none_value({
            "url": url,
            "certificate": certificate,
            "ip_address": ip_address,
            "max_connections": max_connections,
            "allowed_updates": allowed_updates,
            "drop_pending_updates": drop_pending_updates,
            "secret_token": secret_token
        }))

    async def delete_webhook(self, drop_pending_updates=None):
        return await self._client.request_to_api("deleteWebhook", remove_none_value({
            "drop_pending_updates": drop_pending_updates
        }))

    async def get_webhook_info(self):
        return await self._client.request_to_api("getWebhookInfo")

    async def send_message(
            self,
            chat_id,
            text,
            message_thread_id=None,
            parse_mode=None,
            entities=None,
            link_preview_options=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendMessage", remove_none_value({
            "chat_id": chat_id,
            "text": text,
            "message_thread_id": message_thread_id,
            "parse_mode": parse_mode,
            "entities": entities,
            "link_preview_options": link_preview_options,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def forward_message(
            self,
            chat_id,
            from_chat_id,
            message_thread_id=None,
            disable_notification=None,
            protect_content=None,
            message_id=None
    ):
        return await self._client.request_to_api("forwardMessage", remove_none_value({
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "message_id": message_id
        }))

    async def copy_message(
            self,
            chat_id,
            from_chat_id,
            message_id,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("copyMessage", remove_none_value({
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_photo(
            self,
            chat_id,
            photo,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            has_spoiler=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendPhoto", remove_none_value({
            "chat_id": chat_id,
            "photo": photo,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "has_spoiler": has_spoiler,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_audio(
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
            reply_markup=None
    ):
        return await self._client.request_to_api("sendAudio", remove_none_value({
            "chat_id": chat_id,
            "audio": audio,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "performer": performer,
            "title": title,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_document(
            self,
            chat_id,
            document,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            thumbnail=None,
            disable_notification=None,
            disable_content_type_detection=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendDocument", remove_none_value({
            "chat_id": chat_id,
            "document": document,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "disable_content_type_detection": disable_content_type_detection,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_video(
            self,
            chat_id,
            video,
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
            reply_markup=None
    ):
        return await self._client.request_to_api("sendVideo", remove_none_value({
            "chat_id": chat_id,
            "video": video,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "width": width,
            "height": height,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "has_spoiler": has_spoiler,
            "supports_streaming": supports_streaming,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_animation(
            self,
            chat_id,
            animation,
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
            reply_markup=None
    ):
        return await self._client.request_to_api("sendAnimation", remove_none_value({
            "chat_id": chat_id,
            "animation": animation,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "width": width,
            "height": height,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "has_spoiler": has_spoiler,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_voice(
            self,
            chat_id,
            voice,
            message_thread_id=None,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            duration=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendVoice", remove_none_value({
            "chat_id": chat_id,
            "voice": voice,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_video_note(
            self,
            chat_id,
            video_note,
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
            reply_markup=None
    ):
        return await self._client.request_to_api("sendVideoNote", remove_none_value({
            "chat_id": chat_id,
            "video_note": video_note,
            "message_thread_id": message_thread_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "duration": duration,
            "length": length,
            "thumbnail": thumbnail,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_media_group(
            self,
            chat_id,
            media,
            message_thread_id=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None
    ):
        return await self._client.request_to_api("sendMediaGroup", remove_none_value({
            "chat_id": chat_id,
            "media": media,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
        }))

    async def send_location(
            self,
            chat_id,
            latitude,
            longitude,
            message_thread_id=None,
            proximity_alert_radius=None,
            heading=None,
            live_period=None,
            horizontal_accuracy=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendLocation", remove_none_value({
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude,
            "message_thread_id": message_thread_id,
            "proximity_alert_radius": proximity_alert_radius,
            "heading": heading,
            "live_period": live_period,
            "horizontal_accuracy": horizontal_accuracy,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_venue(
            self,
            chat_id,
            latitude,
            longitude,
            title,
            address,
            message_thread_id=None,
            foursquare_id=None,
            foursquare_type=None,
            google_place_id=None,
            google_place_type=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendVenue", remove_none_value({
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude,
            "title": title,
            "address": address,
            "message_thread_id": message_thread_id,
            "foursquare_id": foursquare_id,
            "foursquare_type": foursquare_type,
            "google_place_id": google_place_id,
            "google_place_type": google_place_type,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_contact(
            self,
            chat_id,
            phone_number,
            first_name,
            message_thread_id=None,
            last_name=None,
            vcard=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendContact", remove_none_value({
            "chat_id": chat_id,
            "phone_number": phone_number,
            "first_name": first_name,
            "last_name": last_name,
            "vcard": vcard,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_poll(
            self,
            chat_id,
            question,
            options,
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
            reply_markup=None
    ):
        return await self._client.request_to_api("sendPoll", remove_none_value({
            "chat_id": chat_id,
            "question": question,
            "options": options,
            "message_thread_id": message_thread_id,
            "is_anonymous": is_anonymous,
            "type": poll_type,
            "allows_multiple_answers": allows_multiple_answers,
            "correct_option_id": correct_option_id,
            "explanation": explanation,
            "explanation_parse_mode": explanation_parse_mode,
            "explanation_entities": explanation_entities,
            "open_period": open_period,
            "close_date": close_date,
            "is_closed": is_closed,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_dice(
            self,
            chat_id,
            emoji=None,
            message_thread_id=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendDice", remove_none_value({
            "chat_id": chat_id,
            "emoji": emoji,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup
        }))

    async def send_chat_action(
            self,
            chat_id,
            action,
            message_thread_id=None
    ):
        return await self._client.request_to_api("sendChatAction", remove_none_value({
            "chat_id": chat_id,
            "action": action,
            "message_thread_id": message_thread_id
        }))

    async def get_user_profile_photos(
            self,
            user_id,
            offset=None,
            limit=None
    ):
        return await self._client.request_to_api("getUserProfilePhotos", remove_none_value({
            "user_id": user_id,
            "offset": offset,
            "limit": limit
        }))

    async def get_file(self, file_id):
        return await self._client.request_to_api("getFile", remove_none_value({"file_id": file_id}))

    async def ban_chat_member(
            self,
            chat_id,
            user_id,
            until_date=None,
            revoke_messages=None
    ):
        return await self._client.request_to_api("banChatMember", remove_none_value({
            "chat_id": chat_id,
            "user_id": user_id,
            "until_date": until_date,
            "revoke_messages": revoke_messages
        }))

    async def unban_chat_member(
            self,
            chat_id,
            user_id,
            only_if_banned=None
    ):
        return await self._client.request_to_api("unbanChatMember", remove_none_value({
            "chat_id": chat_id,
            "user_id": user_id,
            "only_if_banned": only_if_banned
        }))

    async def restrict_chat_member(
            self,
            chat_id,
            user_id,
            permissions,
            use_independent_chat_permissions=None,
            until_date=None
    ):
        return await self._client.request_to_api("restrictChatMember", remove_none_value({
            "chat_id": chat_id,
            "user_id": user_id,
            "permissions": permissions,
            "use_independent_chat_permissions": use_independent_chat_permissions,
            "until_date": until_date
        }))

    async def promote_chat_member(
            self,
            chat_id,
            user_id,
            is_anonymous,
            can_manage_chat=None,
            can_delete_messages=None,
            can_manage_video_chats=None,
            can_restrict_members=None,
            can_promote_members=None,
            can_change_info=None,
            can_invite_users=None,
            can_post_messages=None,
            can_edit_messages=None,
            can_pin_messages=None,
            can_post_stories=None,
            can_edit_stories=None,
            can_delete_stories=None,
            can_manage_topics=None
    ):
        return await self._client.request_to_api("promoteChatMember", remove_none_value({
            "chat_id": chat_id,
            "user_id": user_id,
            "is_anonymous": is_anonymous,
            "can_manage_chat": can_manage_chat,
            "can_delete_messages": can_delete_messages,
            "can_manage_video_chats": can_manage_video_chats,
            "can_restrict_members": can_restrict_members,
            "can_promote_members": can_promote_members,
            "can_change_info": can_change_info,
            "can_invite_users": can_invite_users,
            "can_post_messages": can_post_messages,
            "can_edit_messages": can_edit_messages,
            "can_pin_messages": can_pin_messages,
            "can_post_stories": can_post_stories,
            "can_edit_stories": can_edit_stories,
            "can_delete_stories": can_delete_stories,
            "can_manage_topics": can_manage_topics
        }))

    async def set_chat_administrator_custom_title(
            self,
            chat_id,
            user_id,
            custom_title
    ):
        return await self._client.request_to_api("setChatAdministratorCustomTitle", remove_none_value({
            "chat_id": chat_id,
            "user_id": user_id,
            "custom_title": custom_title
        }))

    async def ban_chat_sender_chat(
            self,
            chat_id,
            sender_chat_id
    ):
        return await self._client.request_to_api("banChatSenderChat", remove_none_value({
            "chat_id": chat_id,
            "sender_chat_id": sender_chat_id
        }))

    async def unban_chat_sender_chat(
            self,
            chat_id,
            sender_chat_id
    ):
        return await self._client.request_to_api("unbanChatSenderChat", remove_none_value({
            "chat_id": chat_id, "sender_chat_id": sender_chat_id
        }))

    async def set_chat_permissions(
            self,
            chat_id,
            permissions,
            use_independent_chat_permissions=None
    ):
        return await self._client.request_to_api("setChatPermissions", remove_none_value({
            "chat_id": chat_id,
            "permissions": permissions,
            "use_independent_chat_permissions":
                use_independent_chat_permissions
        }))

    async def export_chat_invite_link(self, chat_id):
        return await self._client.request_to_api("exportChatInviteLink", remove_none_value({
            "chat_id": chat_id
        }))

    async def create_chat_invite_link(
            self,
            chat_id,
            name=None,
            expire_date=None,
            member_limit=None,
            creates_join_request=None
    ):
        return await self._client.request_to_api("createChatInviteLink", remove_none_value({
            "chat_id": chat_id,
            "name": name,
            "expire_date": expire_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request
        }))

    async def edit_chat_invite_link(
            self,
            chat_id,
            invite_link,
            name=None,
            expire_date=None,
            member_limit=None,
            creates_join_request=None
    ):
        return await self._client.request_to_api("editChatInviteLink", remove_none_value({
            "chat_id": chat_id,
            "invite_link": invite_link,
            "name": name,
            "expire_date": expire_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request
        }))

    async def revoke_chat_invite_link(
            self,
            chat_id,
            invite_link
    ):
        return await self._client.request_to_api("revokeChatInviteLink", remove_none_value({
            "chat_id": chat_id,
            "invite_link": invite_link
        }))

    async def approve_chat_join_request(
            self,
            chat_id,
            user_id
    ):
        return await self._client.request_to_api("approveChatJoinRequest", remove_none_value({
            "chat_id": chat_id,
            "user_id": user_id
        }))

    async def decline_chat_join_request(
            self,
            chat_id,
            user_id
    ):
        return await self._client.request_to_api("declineChatJoinRequest", remove_none_value({
            "chat_id": chat_id,
            "user_id": user_id
        }))

    async def set_chat_photo(
            self,
            chat_id,
            photo
    ):
        return await self._client.request_to_api("setChatPhoto", remove_none_value({
            "chat_id": chat_id,
            "photo": photo
        }))

    async def delete_chat_photo(
            self,
            chat_id
    ):
        return await self._client.request_to_api("deleteChatPhoto", remove_none_value({
            "chat_id": chat_id
        }))

    async def set_chat_title(
            self,
            chat_id,
            title
    ):
        return await self._client.request_to_api("setChatTitle", remove_none_value({
            "chat_id": chat_id,
            "title": title
        }))

    async def set_chat_description(
            self,
            chat_id,
            description
    ):
        return await self._client.request_to_api("setChatDescription", remove_none_value({
            "chat_id": chat_id,
            "description": description
        }))

    async def pin_chat_message(
            self,
            chat_id,
            message_id,
            disable_notification
    ):
        return await self._client.request_to_api("pinChatMessage", remove_none_value({
            "chat_id": chat_id,
            "message_id": message_id,
            "disable_notification": disable_notification
        }))

    async def unpin_chat_message(
            self,
            chat_id,
            message_id
    ):
        return await self._client.request_to_api("pinChatMessage", remove_none_value({
            "chat_id": chat_id,
            "message_id": message_id
        }))

    async def leave_chat(
            self,
            chat_id
    ):
        return await self._client.request_to_api("leaveChat", remove_none_value({
            "chat_id": chat_id
        }))

    async def get_chat(
            self,
            chat_id
    ):
        return await self._client.request_to_api("getChat", remove_none_value({
            "chat_id": chat_id
        }))

    async def get_chat_administrators(
            self,
            chat_id
    ):
        return await self._client.request_to_api("getChatAdministrators", remove_none_value({
            "chat_id": chat_id
        })
                                                 )

    async def get_chat_member_count(
            self,
            chat_id
    ):
        return await self._client.request_to_api("getChatMemberCount", remove_none_value({
            "chat_id": chat_id
        }))

    async def get_chat_member(
            self,
            chat_id
    ):
        return await self._client.request_to_api("getChatMember", remove_none_value({
            "chat_id": chat_id
        }))

    async def set_chat_sticker_set(
            self,
            chat_id,
            sticker_set_name
    ):
        return await self._client.request_to_api("setChatStickerSet", remove_none_value({
            "chat_id": chat_id,
            "sticker_set_name": sticker_set_name
        }))

    async def delete_chat_sticker_set(
            self,
            chat_id,
    ):
        return await self._client.request_to_api("deleteChatStickerSet", remove_none_value({
            "chat_id": chat_id
        }))

    async def get_forum_topic_icon_stickers(
            self,
            chat_id,
    ):
        return await self._client.request_to_api("getForumTopicIconStickers", remove_none_value({
            "chat_id": chat_id
        }))

    async def create_forum_topic(
            self,
            chat_id,
            name,
            icon_color=None,
            icon_custom_emoji_id=None
    ):
        return await self._client.request_to_api("createForumTopic", remove_none_value({
            "chat_id": chat_id,
            "name": name,
            "icon_color": icon_color,
            "icon_custom_emoji_id": icon_custom_emoji_id
        }))

    async def edit_forum_topic(
            self,
            chat_id,
            message_thread_id,
            name=None,
            icon_custom_emoji_id=None
    ):
        return await self._client.request_to_api("editForumTopic", remove_none_value({
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "name": name,
            "icon_custom_emoji_id": icon_custom_emoji_id
        }))

    async def close_forum_topic(
            self,
            chat_id,
            message_thread_id
    ):
        return await self._client.request_to_api("closeForumTopic", remove_none_value({
            "chat_id": chat_id,
            "message_thread_id": message_thread_id
        }))

    async def reopen_forum_topic(
            self,
            chat_id,
            message_thread_id
    ):
        return await self._client.request_to_api("reopenForumTopic", remove_none_value({
            "chat_id": chat_id,
            "message_thread_id": message_thread_id
        }))

    async def delete_forum_topic(
            self,
            chat_id,
            message_thread_id
    ):
        return await self._client.request_to_api("deleteForumTopic", remove_none_value({
            "chat_id": chat_id,
            "message_thread_id": message_thread_id
        }))

    async def unpin_all_forum_topic_messages(
            self,
            chat_id,
            message_thread_id
    ):
        return await self._client.request_to_api("unpinAllForumTopicMessages", remove_none_value({
            "chat_id": chat_id,
            "message_thread_id": message_thread_id
        }))

    async def edit_general_forum_topic(
            self,
            chat_id,
            name
    ):
        return await self._client.request_to_api("editGeneralForumTopic", remove_none_value({
            "chat_id": chat_id,
            "name": name
        }))

    async def close_general_forum_topic(
            self,
            chat_id
    ):
        return await self._client.request_to_api("closeGeneralForumTopic", remove_none_value({
            "chat_id": chat_id
        }))

    async def reopen_general_forum_topic(
            self,
            chat_id
    ):
        return await self._client.request_to_api("reopenGeneralForumTopic", remove_none_value({
            "chat_id": chat_id
        }))

    async def hide_general_forum_topic(
            self,
            chat_id
    ):
        return await self._client.request_to_api("hideGeneralForumTopic", remove_none_value({
            "chat_id": chat_id
        }))

    async def unhide_general_forum_topic(
            self,
            chat_id
    ):
        return await self._client.request_to_api("unhideGeneralForumTopic", remove_none_value({
            "chat_id": chat_id
        }))

    async def unpin_all_general_forum_topic_messages(
            self,
            chat_id
    ):
        return await self._client.request_to_api("unpinAllGeneralForumTopicMessages", remove_none_value({
            "chat_id": chat_id
        }))

    async def answer_callback_query(
            self,
            callback_query_id,
            text=None,
            show_alert=None,
            url=None,
            cache_time=None,
    ):
        return await self._client.request_to_api("answerCallbackQuery", remove_none_value({
            "callback_query_id": callback_query_id,
            "text": text,
            "show_alert": show_alert,
            "url": url,
            "cache_time": cache_time,
        }))

    async def set_my_commands(
            self,
            commands,
            scope=None,
            language_code=None
    ):
        return await self._client.request_to_api("setMyCommands", remove_none_value({
            "commands": commands,
            "scope": scope,
            "language_code": language_code
        }))

    async def delete_my_commands(
            self,
            scope=None,
            language_code=None
    ):
        return await self._client.request_to_api("deleteMyCommands", remove_none_value({
            "scope": scope,
            "language_code": language_code
        }))

    async def get_my_commands(
            self,
            scope=None,
            language_code=None
    ):
        return await self._client.request_to_api("getMyCommands", remove_none_value({
            "scope": scope,
            "language_code": language_code
        }))

    async def set_my_name(
            self,
            name=None,
            language_code=None
    ):
        return await self._client.request_to_api("setMyName", remove_none_value({
            "name": name,
            "language_code": language_code
        }))

    async def get_my_name(
            self,
            language_code=None
    ):
        return await self._client.request_to_api("getMyName", remove_none_value({
            "language_code": language_code
        }))

    async def set_my_description(
            self,
            description=None,
            language_code=None
    ):
        return await self._client.request_to_api("setMyDescription", remove_none_value({
            "description": description,
            "language_code": language_code
        }))

    async def get_my_description(
            self,
            language_code=None
    ):
        return await self._client.request_to_api("getMyDescription", remove_none_value({
            "language_code": language_code
        }))

    async def set_my_short_description(
            self,
            short_description=None,
            language_code=None
    ):
        return await self._client.request_to_api("setMyShortDescription", remove_none_value({
            "short_description": short_description,
            "language_code": language_code
        }))

    async def get_my_short_description(
            self,
            language_code=None
    ):
        return await self._client.request_to_api("getMyShortDescription", remove_none_value({
            "language_code": language_code
        }))

    async def set_chat_menu_button(
            self,
            chat_id=None,
            menu_button=None
    ):
        return await self._client.request_to_api("setChatMenuButton", remove_none_value({
            "chat_id": chat_id,
            "menu_button": menu_button
        }))

    async def get_chat_menu_button(
            self,
            chat_id=None
    ):
        return await self._client.request_to_api("getChatMenuButton", remove_none_value({
            "chat_id": chat_id
        }))

    async def set_my_default_administrator_rights(
            self,
            rights=None,
            for_channels=None
    ):
        return await self._client.request_to_api("setMyDefaultAdministratorRights", remove_none_value({
            "rights": rights,
            "for_channels": for_channels
        }))

    async def get_my_default_administrator_rights(
            self,
            for_channels=None
    ):
        return await self._client.request_to_api("getMyDefaultAdministratorRights", remove_none_value({
            "for_channels": for_channels
        }))

    async def edit_message_text(
            self,
            text,
            chat_id=None,
            inline_message_id=None,
            parse_mode=None,
            entities=None,
            link_preview_options=None,
            message_id=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("editMessageText", remove_none_value({
            "chat_id": chat_id,
            "text": text,
            "inline_message_id": inline_message_id,
            "parse_mode": parse_mode,
            "entities": entities,
            "link_preview_options": link_preview_options,
            "message_id": message_id,
            "reply_markup": reply_markup
        }))

    async def edit_message_caption(
            self,
            chat_id=None,
            caption=None,
            inline_message_id=None,
            parse_mode=None,
            caption_entities=None,
            disable_web_page_preview=None,
            message_id=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("editMessageCaption", remove_none_value({
            "chat_id": chat_id,
            "caption": caption,
            "inline_message_id": inline_message_id,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "disable_web_page_preview": disable_web_page_preview,
            "message_id": message_id,
            "reply_markup": reply_markup
        }))

    async def edit_message_media(
            self,
            chat_id=None,
            media=None,
            inline_message_id=None,
            message_id=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("editMessageMedia", remove_none_value({
            "chat_id": chat_id,
            "media": media,
            "inline_message_id": inline_message_id,
            "message_id": message_id,
            "reply_markup": reply_markup
        }))

    async def edit_message_live_location(
            self,
            latitude,
            longitude,
            chat_id=None,
            inline_message_id=None,
            message_id=None,
            message_thread_id=None,
            proximity_alert_radius=None,
            heading=None,
            live_period=None,
            horizontal_accuracy=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("editMessageLiveLocation", remove_none_value({
            "latitude": latitude,
            "longitude": longitude,
            "chat_id": chat_id,
            "inline_message_id": inline_message_id,
            "message_id": message_id,
            "message_thread_id": message_thread_id,
            "proximity_alert_radius": proximity_alert_radius,
            "heading": heading,
            "live_period": live_period,
            "horizontal_accuracy": horizontal_accuracy,
            "reply_markup": reply_markup
        }))

    async def stop_message_live_location(
            self,
            chat_id=None,
            inline_message_id=None,
            message_id=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("editMessageLiveLocation", remove_none_value({
            "chat_id": chat_id,
            "inline_message_id": inline_message_id,
            "message_id": message_id,
            "reply_markup": reply_markup
        }))

    async def edit_message_reply_markup(
            self,
            chat_id=None,
            inline_message_id=None,
            message_id=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("editMessageReplyMarkup", remove_none_value({
            "chat_id": chat_id,
            "inline_message_id": inline_message_id,
            "message_id": message_id,
            "reply_markup": reply_markup
        }))

    async def stop_poll(
            self,
            chat_id,
            message_id,
            reply_markup=None
    ):
        return await self._client.request_to_api("stopPoll", remove_none_value({
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup
        }))

    async def delete_message(
            self,
            chat_id,
            message_id
    ):
        return await self._client.request_to_api("deleteMessage", remove_none_value({
            "chat_id": chat_id,
            "message_id": message_id
        }))

    async def send_sticker(
            self,
            chat_id,
            sticker,
            message_thread_id=None,
            emoji=None,
            disable_notification=None,
            protect_content=None,
            reply_to_message_id=None,
            allow_sending_without_reply=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendSticker", remove_none_value({
            "chat_id": chat_id,
            "sticker": sticker,
            "message_thread_id": message_thread_id,
            "emoji": emoji,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_to_message_id": reply_to_message_id,
            "allow_sending_without_reply": allow_sending_without_reply,
            "reply_markup": reply_markup
        }))

    async def get_sticker_set(
            self,
            name
    ):
        return await self._client.request_to_api("getStickerSet", remove_none_value({
            "name": name
        }))

    async def get_custom_emoji_stickers(
            self,
            custom_emoji_ids
    ):
        return await self._client.request_to_api("getCustomEmojiStickers", remove_none_value({
            "custom_emoji_ids": custom_emoji_ids
        }))

    async def upload_sticker_file(
            self,
            user_id,
            sticker,
            sticker_format
    ):
        return await self._client.request_to_api("uploadStickerFile", remove_none_value({
            "user_id": user_id,
            "sticker": sticker,
            "sticker_format": sticker_format,
        }))

    async def create_new_sticker_set(
            self,
            user_id,
            name,
            title,
            stickers,
            sticker_format,
            sticker_type=None,
            needs_repainting=None
    ):
        return await self._client.request_to_api("createNewStickerSet", remove_none_value({
            "user_id": user_id,
            "name": name,
            "title": title,
            "stickers": stickers,
            "sticker_format": sticker_format,
            "sticker_type": sticker_type,
            "needs_repainting": needs_repainting,
        }))

    async def add_sticker_to_set(
            self,
            user_id,
            name,
            sticker
    ):
        return await self._client.request_to_api("addStickerToSet", remove_none_value({
            "user_id": user_id,
            "name": name,
            "sticker": sticker
        }))

    async def set_sticker_position_in_set(
            self,
            sticker,
            position
    ):
        return await self._client.request_to_api("setStickerPositionInSet", remove_none_value({
            "sticker": sticker,
            "position": position
        }))

    async def delete_sticker_from_set(
            self,
            sticker,
    ):
        return await self._client.request_to_api("deleteStickerFromSet", remove_none_value({
            "sticker": sticker,
        }))

    async def set_sticker_emoji_list(
            self,
            sticker,
            emoji_list
    ):
        return await self._client.request_to_api("setStickerEmojiList", remove_none_value({
            "sticker": sticker,
            "emoji_list": emoji_list
        }))

    async def set_sticker_keywords(
            self,
            sticker,
            keywords=None
    ):
        return await self._client.request_to_api("setStickerKeywords", remove_none_value({
            "sticker": sticker,
            "keywords": keywords
        }))

    async def set_sticker_mask_position(
            self,
            sticker,
            mask_position=None
    ):
        return await self._client.request_to_api("setStickerMaskPosition", remove_none_value({
            "sticker": sticker,
            "mask_position": mask_position
        }))

    async def set_sticker_set_title(
            self,
            name,
            title
    ):
        return await self._client.request_to_api("setStickerSetTitle", remove_none_value({
            "name": name,
            "title": title
        }))

    async def set_sticker_set_thumbnail(
            self,
            name,
            user_id,
            thumbnail=None
    ):
        return await self._client.request_to_api("setStickerSetThumbnail", remove_none_value({
            "name": name,
            "user_id": user_id,
            "thumbnail": thumbnail
        }))

    async def set_custom_emoji_sticker_set_thumbnail(
            self,
            name,
            custom_emoji_id=None
    ):
        return await self._client.request_to_api("setCustomEmojiStickerSetThumbnail", remove_none_value({
            "name": name,
            "custom_emoji_id": custom_emoji_id
        }))

    async def delete_sticker_set(
            self,
            name
    ):
        return await self._client.request_to_api("deleteStickerSet", remove_none_value({
            "name": name
        }))

    async def answer_inline_query(
            self,
            inline_query_id,
            results,
            cache_time=None,
            is_personal=None,
            next_offset=None,
            button=None
    ):
        return await self._client.request_to_api("answerInlineQuery", remove_none_value({
            "inline_query_id": inline_query_id,
            "results": results,
            "cache_time": cache_time,
            "is_personal": is_personal,
            "next_offset": next_offset,
            "button": button
        }))

    async def answer_web_app_query(
            self,
            web_app_query_id,
            result
    ):
        return await self._client.request_to_api("answerWebAppQuery", remove_none_value({
            "web_app_query_id": web_app_query_id,
            "result": result
        }))

    async def send_invoice(
            self,
            chat_id,
            title,
            description,
            payload,
            provider_token,
            currency,
            prices,
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
        return await self._client.request_to_api("sendInvoice", remove_none_value({
            "chat_id": chat_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": provider_token,
            "currency": currency,
            "prices": prices,
            "message_thread_id": message_thread_id,
            "max_tip_amount": max_tip_amount,
            "suggested_tip_amounts": suggested_tip_amounts,
            "start_parameter": start_parameter,
            "provider_data": provider_data,
            "photo_url": photo_url,
            "photo_size": photo_size,
            "photo_width": photo_width,
            "photo_height": photo_height,
            "need_name": need_name,
            "need_phone_number": need_phone_number,
            "need_email": need_email,
            "need_shipping_address": need_shipping_address,
            "send_phone_number_to_provider": send_phone_number_to_provider,
            "send_email_to_provider": send_email_to_provider,
            "is_flexible": is_flexible,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup}))

    async def create_invoice_link(
            self,
            title,
            description,
            payload,
            provider_token,
            currency,
            prices,
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
    ):
        return await self._client.request_to_api("createInvoiceLink", remove_none_value({
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": provider_token,
            "currency": currency,
            "prices": prices,
            "message_thread_id": message_thread_id,
            "max_tip_amount": max_tip_amount,
            "suggested_tip_amounts": suggested_tip_amounts,
            "start_parameter": start_parameter,
            "provider_data": provider_data,
            "photo_url": photo_url,
            "photo_size": photo_size,
            "photo_width": photo_width,
            "photo_height": photo_height,
            "need_name": need_name,
            "need_phone_number": need_phone_number,
            "need_email": need_email,
            "need_shipping_address": need_shipping_address,
            "send_phone_number_to_provider": send_phone_number_to_provider,
            "send_email_to_provider": send_email_to_provider,
            "is_flexible": is_flexible}))

    async def answer_shipping_query(
            self,
            shipping_query_id,
            ok,
            shipping_options=None,
            error_message=None
    ):
        return await self._client.request_to_api("answerShippingQuery", remove_none_value({
            "shipping_query_id": shipping_query_id,
            "ok": ok,
            "shipping_options": shipping_options,
            "error_message": error_message
        }))

    async def answer_pre_checkout_query(
            self,
            pre_checkout_query_id,
            ok,
            error_message=None
    ):
        return await self._client.request_to_api("answerPreCheckoutQuery", remove_none_value({
            "pre_checkout_query_id": pre_checkout_query_id,
            "ok": ok,
            "error_message": error_message
        }))

    async def set_passport_data_errors(
            self,
            user_id,
            errors
    ):
        return await self._client.request_to_api("setPassportDataErrors", remove_none_value({
            "user_id": user_id,
            "errors": errors
        }))

    async def send_game(
            self,
            chat_id,
            game_short_name,
            message_thread_id=None,
            disable_notification=None,
            protect_content=None,
            reply_parameters=None,
            reply_markup=None
    ):
        return await self._client.request_to_api("sendGame", remove_none_value({
            "chat_id": chat_id,
            "game_short_name": game_short_name,
            "message_thread_id": message_thread_id,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup}))

    async def set_game_score(
            self,
            user_id,
            score,
            force=None,
            disable_edit_message=None,
            chat_id=None,
            message_id=None,
            inline_message_id=None
    ):
        return await self._client.request_to_api("setGameScore", remove_none_value({
            "user_id": user_id,
            "score": score,
            "force": force,
            "disable_edit_message": disable_edit_message,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id}))

    async def get_game_high_scores(
            self,
            user_id,
            chat_id=None,
            message_id=None,
            inline_message_id=None
    ):
        return await self._client.request_to_api("getGameHighScores", remove_none_value({
            "user_id": user_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_message_id": inline_message_id}))

    async def set_message_reaction(
            self,
            chat_id,
            message_id=None,
            reaction=None,
            is_big=None
    ):
        return await self._client.request_to_api("setMessageReaction", remove_none_value({
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction": reaction,
            "is_big": is_big}))

    async def delete_messages(
            self,
            chat_id,
            message_ids=None
    ):
        return await self._client.request_to_api("deleteMessages", remove_none_value({
            "chat_id": chat_id,
            "message_ids": message_ids}))
