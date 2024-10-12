QT += network

HEADERS += \
# Models
    $${PWD}/OAIAction.h \
    $${PWD}/OAIAnswer.h \
    $${PWD}/OAICreativeWork.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentifiable.h \
    $${PWD}/OAIQueryContext.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponseBase.h \
    $${PWD}/OAISearchAction.h \
    $${PWD}/OAISearchResultsAnswer.h \
    $${PWD}/OAISuggestions.h \
    $${PWD}/OAISuggestionsSuggestionGroup.h \
    $${PWD}/OAIThing.h \
# APIs
    $${PWD}/OAIAutoSuggestApi.h \
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
    $${PWD}/OAIAction.cpp \
    $${PWD}/OAIAnswer.cpp \
    $${PWD}/OAICreativeWork.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentifiable.cpp \
    $${PWD}/OAIQueryContext.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponseBase.cpp \
    $${PWD}/OAISearchAction.cpp \
    $${PWD}/OAISearchResultsAnswer.cpp \
    $${PWD}/OAISuggestions.cpp \
    $${PWD}/OAISuggestionsSuggestionGroup.cpp \
    $${PWD}/OAIThing.cpp \
# APIs
    $${PWD}/OAIAutoSuggestApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
