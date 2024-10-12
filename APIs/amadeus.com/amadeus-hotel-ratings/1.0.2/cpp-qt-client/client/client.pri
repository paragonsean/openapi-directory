QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollectionMeta.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIError400.h \
    $${PWD}/OAIError401.h \
    $${PWD}/OAIError500.h \
    $${PWD}/OAIErrorSource.h \
    $${PWD}/OAIHotelSentiment.h \
    $${PWD}/OAIHotelSentiment_sentiments.h \
    $${PWD}/OAISuccessSentiments.h \
    $${PWD}/OAIWarning.h \
    $${PWD}/OAIWarningNotFound.h \
# APIs
    $${PWD}/OAIHotelRatingsApi.h \
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
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollectionMeta.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError400.cpp \
    $${PWD}/OAIError401.cpp \
    $${PWD}/OAIError500.cpp \
    $${PWD}/OAIErrorSource.cpp \
    $${PWD}/OAIHotelSentiment.cpp \
    $${PWD}/OAIHotelSentiment_sentiments.cpp \
    $${PWD}/OAISuccessSentiments.cpp \
    $${PWD}/OAIWarning.cpp \
    $${PWD}/OAIWarningNotFound.cpp \
# APIs
    $${PWD}/OAIHotelRatingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
