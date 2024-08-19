QT += network

HEADERS += \
# Models
    $${PWD}/OAIChapterSchema.h \
    $${PWD}/OAIVerseSchema.h \
# APIs
    $${PWD}/OAIAuthApi.h \
    $${PWD}/OAIChapterApi.h \
    $${PWD}/OAIVerseApi.h \
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
    $${PWD}/OAIChapterSchema.cpp \
    $${PWD}/OAIVerseSchema.cpp \
# APIs
    $${PWD}/OAIAuthApi.cpp \
    $${PWD}/OAIChapterApi.cpp \
    $${PWD}/OAIVerseApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
