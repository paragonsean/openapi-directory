QT += network

HEADERS += \
# Models
    $${PWD}/OAIChannel_enum_channel_type.h \
    $${PWD}/OAIChannel_enum_webhook_enabled_type.h \
    $${PWD}/OAIChat_v3_channel.h \
# APIs
    $${PWD}/OAIChatV3ChannelApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIChannel_enum_channel_type.cpp \
    $${PWD}/OAIChannel_enum_webhook_enabled_type.cpp \
    $${PWD}/OAIChat_v3_channel.cpp \
# APIs
    $${PWD}/OAIChatV3ChannelApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
