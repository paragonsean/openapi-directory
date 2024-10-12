QT += network

HEADERS += \
# Models
    $${PWD}/OAIAgeAnswer.h \
    $${PWD}/OAIPerson.h \
    $${PWD}/OAITask.h \
    $${PWD}/OAI_adult_content_post_request.h \
    $${PWD}/OAI_artistic_image_post_request.h \
# APIs
    $${PWD}/OAICreativeApi.h \
    $${PWD}/OAIVisionApi.h \
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
    $${PWD}/OAIAgeAnswer.cpp \
    $${PWD}/OAIPerson.cpp \
    $${PWD}/OAITask.cpp \
    $${PWD}/OAI_adult_content_post_request.cpp \
    $${PWD}/OAI_artistic_image_post_request.cpp \
# APIs
    $${PWD}/OAICreativeApi.cpp \
    $${PWD}/OAIVisionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
