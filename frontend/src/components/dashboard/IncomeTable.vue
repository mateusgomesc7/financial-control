<template>
  <v-data-table
    :headers="headers"
    :items="incomes"
    items-per-page="-1"
    height="300"
    hover
    hide-default-footer
    disable-sort
    fixed-header
    class="custom-scroll"
  />
</template>

<script setup lang="ts">
interface Header {
  title: string;
  value: string;
  align?: "start" | "center" | "end";
}

const headers: Header[] = [
  { title: "Renda", value: "name", align: "start" },
  { title: "Valor", value: "value", align: "center" },
];
const incomes = ref([
  { name: "Salário Líquido", value: 3000 },
  { name: "Salário Líquido", value: 5000 },
  { name: "Renda Extra", value: 500 },
  { name: "Renda Extra", value: 300 },
  { name: "Renda Extra", value: 300 },
  { name: "Renda Extra", value: 300 },
  { name: "Renda Extra", value: 300 }
]);
</script>

<style scoped>
:deep(.v-data-table-header__content) {
  font-weight: bold;
  color: rgb(var(--v-theme-primary));
}

:deep(.v-data-table__td) {
  color: rgb(var(--v-theme-primary)) !important;
}

.custom-scroll:deep(.v-table__wrapper) {
  max-height: 300px;
  overflow-y: auto;
}
.custom-scroll:deep(.v-table__wrapper)::-webkit-scrollbar {
  width: 8px;
}
.custom-scroll:deep(.v-table__wrapper)::-webkit-scrollbar-thumb {
  background-color: rgb(var(--v-theme-primary));
  border-radius: 10px;
}
.custom-scroll:deep(.v-table__wrapper)::-webkit-scrollbar-track {
  background-color: #f1f1f1;
}
</style>
