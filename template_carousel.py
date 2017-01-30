from linebot.models import CarouselColumn
from linebot.models import CarouselTemplate
from linebot.models import MessageTemplateAction
from linebot.models import PostbackTemplateAction
from linebot.models import TemplateSendMessage
from linebot.models import URITemplateAction

carousels = [{
    "id" : "example",
    "payload" : TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item1.jpg',
                    title='Transportasi & Travel',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageTemplateAction(
                            label='message1',
                            text='message text1'
                        ),
                        URITemplateAction(
                            label='uri1',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='BJPay',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='http://example.com/2'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='Pulsa',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback3',
                            text='postback text3',
                            data='action=buy&itemid=3'
                        ),
                        MessageTemplateAction(
                            label='message3',
                            text='message text3'
                        ),
                        URITemplateAction(
                            label='uri3',
                            uri='http://example.com/2'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='Info',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback4',
                            text='postback text4',
                            data='action=buy&itemid=4'
                        ),
                        MessageTemplateAction(
                            label='message4',
                            text='message text4'
                        ),
                        URITemplateAction(
                            label='uri4',
                            uri='http://example.com/2'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='Others',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback5',
                            text='postback text5',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message5',
                            text='message text5'
                        ),
                        URITemplateAction(
                            label='uri5',
                            uri='http://example.com/2'
                        )
                    ]
                )
            ]
        )
    )
},{
"id" : "greetings",
    "payload" : TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='http://bangjoni.com/v2/carousel/greetings/travel.png',
                    title='Transportasi & Travel',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageTemplateAction(
                            label='message1',
                            text='message text1'
                        ),
                        URITemplateAction(
                            label='uri1',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://bangjoni.com/v2/carousel/greetings/bjpay.png',
                    title='BJPay',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='http://example.com/2'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://bangjoni.com/v2/carousel/greetings/pulsa.png',
                    title='Pulsa',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback3',
                            text='postback text3',
                            data='action=buy&itemid=3'
                        ),
                        MessageTemplateAction(
                            label='message3',
                            text='message text3'
                        ),
                        URITemplateAction(
                            label='uri3',
                            uri='http://example.com/2'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://bangjoni.com/v2/carousel/greetings/info.png',
                    title='Info',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback4',
                            text='postback text4',
                            data='action=buy&itemid=4'
                        ),
                        MessageTemplateAction(
                            label='message4',
                            text='message text4'
                        ),
                        URITemplateAction(
                            label='uri4',
                            uri='http://example.com/2'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://bangjoni.com/v2/carousel/greetings/other.png',
                    title='Others',
                    text='blah',
                    actions=[
                        PostbackTemplateAction(
                            label='postback5',
                            text='postback text5',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message5',
                            text='message text5'
                        ),
                        URITemplateAction(
                            label='uri5',
                            uri='http://example.com/2'
                        )
                    ]
                )
            ]
        )
    )
}]

def composeCarousel(alt_text, columns):
    carousel_columns = []
    for column in columns:
        actions = []
        for action in column['actions']:
            if action['type'] == 'postback':
                actions.append(PostbackTemplateAction(label=action['label'], text=action['text'], data=action['data']))
            elif action['type'] == 'message':
                actions.append(MessageTemplateAction(label=action['label'], text=action['text']))
            elif action['type'] == 'uri':
                actions.append(URITemplateAction(label=action['label'], uri=action['uri']))
        col = CarouselColumn(thumbnail_image_url=column['thumbnail_image_url'], title=column['title'], text=column['text'], actions=actions)
        carousel_columns.append(col)
    template = TemplateSendMessage(alt_text=alt_text, template=CarouselColumn(columns=carousel_columns))
    return template