QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiResponseFailure.h \
    $${PWD}/OAIApiResponseSuccess.h \
    $${PWD}/OAIChromeAdvancedOptions.h \
    $${PWD}/OAIChromeHtmlToPdfRequest.h \
    $${PWD}/OAIChromeUrlToPdfRequest.h \
    $${PWD}/OAILibreOfficeConvertRequest.h \
    $${PWD}/OAIMergeRequest.h \
    $${PWD}/OAIWkHtmlToPdfAdvancedOptions.h \
    $${PWD}/OAIWkHtmlToPdfHtmlToPdfRequest.h \
    $${PWD}/OAIWkHtmlToPdfUrlToPdfRequest.h \
# APIs
    $${PWD}/OAIHeadlessChromeApi.h \
    $${PWD}/OAILibreOfficeApi.h \
    $${PWD}/OAIMergeCombinePdfsApi.h \
    $${PWD}/OAIWkhtmltopdfApi.h \
    $${PWD}/OAIZXINGZebraCrossingBarCodesApi.h \
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
    $${PWD}/OAIApiResponseFailure.cpp \
    $${PWD}/OAIApiResponseSuccess.cpp \
    $${PWD}/OAIChromeAdvancedOptions.cpp \
    $${PWD}/OAIChromeHtmlToPdfRequest.cpp \
    $${PWD}/OAIChromeUrlToPdfRequest.cpp \
    $${PWD}/OAILibreOfficeConvertRequest.cpp \
    $${PWD}/OAIMergeRequest.cpp \
    $${PWD}/OAIWkHtmlToPdfAdvancedOptions.cpp \
    $${PWD}/OAIWkHtmlToPdfHtmlToPdfRequest.cpp \
    $${PWD}/OAIWkHtmlToPdfUrlToPdfRequest.cpp \
# APIs
    $${PWD}/OAIHeadlessChromeApi.cpp \
    $${PWD}/OAILibreOfficeApi.cpp \
    $${PWD}/OAIMergeCombinePdfsApi.cpp \
    $${PWD}/OAIWkhtmltopdfApi.cpp \
    $${PWD}/OAIZXINGZebraCrossingBarCodesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
