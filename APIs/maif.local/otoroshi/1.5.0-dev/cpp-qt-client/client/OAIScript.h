/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIScript.h
 *
 * A script to transformer otoroshi requests 
 */

#ifndef OAIScript_H
#define OAIScript_H

#include <QJsonObject>

#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIScript : public OAIObject {
public:
    OAIScript();
    OAIScript(QString json);
    ~OAIScript() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, QString> getCode() const;
    void setCode(const QMap<QString, QString> &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QMap<QString, QString> getDesc() const;
    void setDesc(const QMap<QString, QString> &desc);
    bool is_desc_Set() const;
    bool is_desc_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, QString> m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QMap<QString, QString> m_desc;
    bool m_desc_isSet;
    bool m_desc_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScript)

#endif // OAIScript_H
