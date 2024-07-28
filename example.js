const app = new Vue({
  el: "#todoapp",
  data: {
    //  总数据
    todoList: ["Eating", "Sleeping", "Reading"],
    //  输入的内容
    inputValue: "",
  },
  // 方法
  methods: {
    // 增加任务
    addTodo() {
      this.todoList.push(this.inputValue);
    },
    // 删除任务
    delTodo(index) {
      this.todoList.splice(index, 1);
    },
    clearTodo() {
      this.todoList = [];
    }
  }
});
