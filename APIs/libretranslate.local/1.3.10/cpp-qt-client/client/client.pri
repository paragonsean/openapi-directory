QT += network

HEADERS += \
# Models
    $${PWD}/OAIDetections_inner.h \
    $${PWD}/OAIError_response.h \
    $${PWD}/OAIError_slow_down.h \
    $${PWD}/OAIFrontend_settings.h \
    $${PWD}/OAIFrontend_settings_language.h \
    $${PWD}/OAIFrontend_settings_language_source.h \
    $${PWD}/OAILanguages_inner.h \
    $${PWD}/OAISuggest_response.h \
    $${PWD}/OAITranslate.h \
    $${PWD}/OAITranslate_file.h \
    $${PWD}/OAITranslate_translatedText.h \
# APIs
    $${PWD}/OAIFeedbackApi.h \
    $${PWD}/OAIFrontendApi.h \
    $${PWD}/OAITranslateApi.h \
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
    $${PWD}/OAIDetections_inner.cpp \
    $${PWD}/OAIError_response.cpp \
    $${PWD}/OAIError_slow_down.cpp \
    $${PWD}/OAIFrontend_settings.cpp \
    $${PWD}/OAIFrontend_settings_language.cpp \
    $${PWD}/OAIFrontend_settings_language_source.cpp \
    $${PWD}/OAILanguages_inner.cpp \
    $${PWD}/OAISuggest_response.cpp \
    $${PWD}/OAITranslate.cpp \
    $${PWD}/OAITranslate_file.cpp \
    $${PWD}/OAITranslate_translatedText.cpp \
# APIs
    $${PWD}/OAIFeedbackApi.cpp \
    $${PWD}/OAIFrontendApi.cpp \
    $${PWD}/OAITranslateApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
