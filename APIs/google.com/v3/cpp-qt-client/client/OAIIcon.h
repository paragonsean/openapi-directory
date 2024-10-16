/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIcon.h
 *
 * Information about a partner&#39;s icon.
 */

#ifndef OAIIcon_H
#define OAIIcon_H

#include <QJsonObject>

#include <QByteArray>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIcon : public OAIObject {
public:
    OAIIcon();
    OAIIcon(QString json);
    ~OAIIcon() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getDisapprovalReasons() const;
    void setDisapprovalReasons(const QList<QString> &disapproval_reasons);
    bool is_disapproval_reasons_Set() const;
    bool is_disapproval_reasons_Valid() const;

    QString getIconUri() const;
    void setIconUri(const QString &icon_uri);
    bool is_icon_uri_Set() const;
    bool is_icon_uri_Valid() const;

    QByteArray getImageData() const;
    void setImageData(const QByteArray &image_data);
    bool is_image_data_Set() const;
    bool is_image_data_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getReference() const;
    void setReference(const QString &reference);
    bool is_reference_Set() const;
    bool is_reference_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_disapproval_reasons;
    bool m_disapproval_reasons_isSet;
    bool m_disapproval_reasons_isValid;

    QString m_icon_uri;
    bool m_icon_uri_isSet;
    bool m_icon_uri_isValid;

    QByteArray m_image_data;
    bool m_image_data_isSet;
    bool m_image_data_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_reference;
    bool m_reference_isSet;
    bool m_reference_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIcon)

#endif // OAIIcon_H
