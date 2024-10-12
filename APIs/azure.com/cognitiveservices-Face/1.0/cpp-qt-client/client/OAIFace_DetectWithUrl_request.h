/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFace_DetectWithUrl_request.h
 *
 * 
 */

#ifndef OAIFace_DetectWithUrl_request_H
#define OAIFace_DetectWithUrl_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFace_DetectWithUrl_request : public OAIObject {
public:
    OAIFace_DetectWithUrl_request();
    OAIFace_DetectWithUrl_request(QString json);
    ~OAIFace_DetectWithUrl_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFace_DetectWithUrl_request)

#endif // OAIFace_DetectWithUrl_request_H
