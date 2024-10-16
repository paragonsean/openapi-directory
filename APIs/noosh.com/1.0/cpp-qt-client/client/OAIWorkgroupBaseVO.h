/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWorkgroupBaseVO.h
 *
 * Java type: com.noosh.nooshapi.vo.WorkgroupBaseVO
 */

#ifndef OAIWorkgroupBaseVO_H
#define OAIWorkgroupBaseVO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWorkgroupBaseVO : public OAIObject {
public:
    OAIWorkgroupBaseVO();
    OAIWorkgroupBaseVO(QString json);
    ~OAIWorkgroupBaseVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getWorkgroupId() const;
    void setWorkgroupId(const qint64 &workgroup_id);
    bool is_workgroup_id_Set() const;
    bool is_workgroup_id_Valid() const;

    QString getWorkgroupName() const;
    void setWorkgroupName(const QString &workgroup_name);
    bool is_workgroup_name_Set() const;
    bool is_workgroup_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_workgroup_id;
    bool m_workgroup_id_isSet;
    bool m_workgroup_id_isValid;

    QString m_workgroup_name;
    bool m_workgroup_name_isSet;
    bool m_workgroup_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWorkgroupBaseVO)

#endif // OAIWorkgroupBaseVO_H
