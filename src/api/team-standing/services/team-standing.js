'use strict';

/**
 * team-standing service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::team-standing.team-standing');
