QT += network

HEADERS += \
# Models
    $${PWD}/OAIAirline.h \
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollection_Meta.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAISuccess_Things.h \
# APIs
    $${PWD}/OAIAirlinesApi.h \
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
    $${PWD}/OAIAirline.cpp \
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollection_Meta.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAISuccess_Things.cpp \
# APIs
    $${PWD}/OAIAirlinesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
