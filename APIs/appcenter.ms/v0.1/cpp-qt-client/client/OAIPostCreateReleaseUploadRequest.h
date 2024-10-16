/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPostCreateReleaseUploadRequest.h
 *
 * 
 */

#ifndef OAIPostCreateReleaseUploadRequest_H
#define OAIPostCreateReleaseUploadRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPostCreateReleaseUploadRequest : public OAIObject {
public:
    OAIPostCreateReleaseUploadRequest();
    OAIPostCreateReleaseUploadRequest(QString json);
    ~OAIPostCreateReleaseUploadRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBuildNumber() const;
    void setBuildNumber(const QString &build_number);
    bool is_build_number_Set() const;
    bool is_build_number_Valid() const;

    QString getBuildVersion() const;
    void setBuildVersion(const QString &build_version);
    bool is_build_version_Set() const;
    bool is_build_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_build_number;
    bool m_build_number_isSet;
    bool m_build_number_isValid;

    QString m_build_version;
    bool m_build_version_isSet;
    bool m_build_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPostCreateReleaseUploadRequest)

#endif // OAIPostCreateReleaseUploadRequest_H
