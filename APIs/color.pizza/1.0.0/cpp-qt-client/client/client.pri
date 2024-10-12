QT += network

HEADERS += \
# Models
    $${PWD}/OAIColor.h \
    $${PWD}/OAIColorBase.h \
    $${PWD}/OAIColorBase_swatchImg.h \
    $${PWD}/OAIColor_hsl.h \
    $${PWD}/OAIColor_lab.h \
    $${PWD}/OAIColor_rgb.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIListDescription.h \
    $${PWD}/OAIPossibleLists.h \
    $${PWD}/OAI__get_200_response.h \
    $${PWD}/OAI_lists__get_200_response.h \
    $${PWD}/OAI_lists__get_200_response_listDescriptions.h \
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
    $${PWD}/OAIColor.cpp \
    $${PWD}/OAIColorBase.cpp \
    $${PWD}/OAIColorBase_swatchImg.cpp \
    $${PWD}/OAIColor_hsl.cpp \
    $${PWD}/OAIColor_lab.cpp \
    $${PWD}/OAIColor_rgb.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIListDescription.cpp \
    $${PWD}/OAIPossibleLists.cpp \
    $${PWD}/OAI__get_200_response.cpp \
    $${PWD}/OAI_lists__get_200_response.cpp \
    $${PWD}/OAI_lists__get_200_response_listDescriptions.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
