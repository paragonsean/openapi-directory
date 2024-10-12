QT += network

HEADERS += \
# Models
    $${PWD}/OAICategory.h \
    $${PWD}/OAICategoryResults.h \
    $${PWD}/OAIFullCategory.h \
    $${PWD}/OAILaw.h \
    $${PWD}/OAILawReference.h \
    $${PWD}/OAILawResult.h \
    $${PWD}/OAILawTopics.h \
    $${PWD}/OAILawType.h \
    $${PWD}/OAILawsResponse.h \
    $${PWD}/OAIMetadata.h \
    $${PWD}/OAIPoc.h \
    $${PWD}/OAIPocResults.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAICategory.cpp \
    $${PWD}/OAICategoryResults.cpp \
    $${PWD}/OAIFullCategory.cpp \
    $${PWD}/OAILaw.cpp \
    $${PWD}/OAILawReference.cpp \
    $${PWD}/OAILawResult.cpp \
    $${PWD}/OAILawTopics.cpp \
    $${PWD}/OAILawType.cpp \
    $${PWD}/OAILawsResponse.cpp \
    $${PWD}/OAIMetadata.cpp \
    $${PWD}/OAIPoc.cpp \
    $${PWD}/OAIPocResults.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
