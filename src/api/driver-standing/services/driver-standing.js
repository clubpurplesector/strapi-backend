'use strict';

/**
 * driver-standing service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::driver-standing.driver-standing');
