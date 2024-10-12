QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnswer.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentifiable.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponseBase.h \
    $${PWD}/OAISpellCheck.h \
    $${PWD}/OAISpellingFlaggedToken.h \
    $${PWD}/OAISpellingTokenSuggestion.h \
# APIs
    $${PWD}/OAISpellCheckApi.h \
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
    $${PWD}/OAIAnswer.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentifiable.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponseBase.cpp \
    $${PWD}/OAISpellCheck.cpp \
    $${PWD}/OAISpellingFlaggedToken.cpp \
    $${PWD}/OAISpellingTokenSuggestion.cpp \
# APIs
    $${PWD}/OAISpellCheckApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
