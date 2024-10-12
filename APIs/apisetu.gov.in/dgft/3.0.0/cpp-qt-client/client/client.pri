QT += network

HEADERS += \
# Models
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_200_response.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_200_response_branch_inner.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_200_response_directors_inner.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_400_response.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_401_response.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_404_response.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_500_response.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_502_response.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_503_response.h \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_504_response.h \
# APIs
    $${PWD}/OAIAPIsApi.h \
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
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_200_response.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_200_response_branch_inner.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_200_response_directors_inner.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_400_response.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_401_response.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_404_response.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_500_response.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_502_response.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_503_response.cpp \
    $${PWD}/OAIImporter_Exporter_Code_Verification_API_504_response.cpp \
# APIs
    $${PWD}/OAIAPIsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
