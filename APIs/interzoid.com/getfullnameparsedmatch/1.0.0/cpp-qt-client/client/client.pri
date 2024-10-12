QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetfullnameparsedmatch_200_response.h \
# APIs
    $${PWD}/OAIFullNameParsedSimilarityKeyApi.h \
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
    $${PWD}/OAIGetfullnameparsedmatch_200_response.cpp \
# APIs
    $${PWD}/OAIFullNameParsedSimilarityKeyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
